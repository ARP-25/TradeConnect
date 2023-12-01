from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.generic import DeleteView, TemplateView
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg
from PIL import Image
from .models import TradePost, Rating, ContactMessage
from .forms import CommentForm, TradePostForm



class TradePostList(generic.ListView):

    model = TradePost
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = TradePost.objects.filter(status=1)
        sort_by = self.request.GET.get('sort_by')

        if sort_by == 'old_to_new':
            queryset = queryset.order_by('created_at')  
        elif sort_by == 'new_to_old':
            queryset = queryset.order_by('-created_at')  

        elif sort_by == 'highest_rated':
            queryset = TradePost.objects.annotate(avg_rating=Avg('ratings__rating')).exclude(avg_rating=0).order_by('-avg_rating')
        elif sort_by == 'lowest_rated':
            queryset = TradePost.objects.annotate(avg_rating=Avg('ratings__rating')).exclude(avg_rating=0).order_by('avg_rating')

        elif sort_by == 'user_posts':
            if self.request.user.is_authenticated:
                queryset = queryset.filter(author=self.request.user)
            else:
                return TradePost.objects.none()  
          
        return queryset


class TradePostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = TradePost.objects.filter(status=1)
        tradepost = get_object_or_404(queryset, slug=slug)
        comments = tradepost.comments.filter(approved=True).order_by('created_at')

        existing_rating = False
        if request.user.is_authenticated:
            existing_rating = Rating.objects.filter(post=tradepost, user=request.user).exists()


        return render(
            request,
            "tradepost_detail.html",
            {
                "tradepost": tradepost, "comments": comments,"commented": False, "existing_rating": existing_rating, "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = TradePost.objects.filter(status=1)
        tradepost = get_object_or_404(queryset, slug=slug)
        comments = tradepost.comments.filter(approved=True).order_by('created_at')


        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.tradepost = tradepost
            comment.save()
            messages.success(request, 'Your comment has been added successfully and will showcase after approval!')
        else:
            comment_form = CommentForm()


        return render(
            request,
            "tradepost_detail.html",
            {
                "tradepost": tradepost, "comments": comments,"commented": True, "comment_form": CommentForm()
            },
        )

class TradePostRating(View):

    def post(self, request, slug):
        tradepost = get_object_or_404(TradePost, slug=slug)
        existing_rating = Rating.objects.filter(post=tradepost, user=request.user).first()

        if existing_rating:
            messages.warning(request, 'You have already rated this trade post.')
            return HttpResponseRedirect(reverse('tradepost_detail', args=[slug]))
      
        rating_value = request.POST.get('rating')

        new_rating = Rating.objects.create(
            post=tradepost,
            user=request.user,
            rating=rating_value
        )

        existing_rating = True
        messages.success(request, 'Thank you for rating this trade post!')
        return HttpResponseRedirect(reverse('tradepost_detail', args=[slug]))


class TradePostDelete(View):

    def post(self, request, slug):
        tradepost = get_object_or_404(TradePost, slug=slug)

        try:
            tradepost.delete()
            messages.success(request, 'Trade Post has been deleted!')
        except Exception as e:
            messages.error(request, f"Error deleting Trade Post: {e}")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))


class TradePostCreate(View):
    template_name = 'tradepost_create.html'

    def get(self, request):
        form = TradePostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TradePostForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            slug = form.cleaned_data['title']
            description = form.cleaned_data['description']
            author = request.user
            trade_image = request.FILES['trade_image']

            trade_post = TradePost.objects.create(
                title=title,
                slug = slugify(title),
                description=description,
                author=author,
                trade_image=trade_image
            )

            messages.success(request, 'Successfully added a TradePost. Awaiting approval before publishing.')
            return HttpResponseRedirect(reverse('home'))  

        else:
            print(form.errors)  
            return render(request, self.template_name, {'form': form})


class TradePostEdit(View):
    template_name = 'tradepost_edit.html'  

    def get(self, request, trade_post_slug):  
        trade_post = get_object_or_404(TradePost, slug=trade_post_slug)
        form = TradePostForm(instance=trade_post)
        return render(request, self.template_name, {'form': form,'trade_post': trade_post})

    def post(self, request, trade_post_slug):  
        trade_post = get_object_or_404(TradePost, slug=trade_post_slug)
        form = TradePostForm(request.POST, instance=trade_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited a TradePost.')
            return HttpResponseRedirect(reverse('home'))  
        return render(request, self.template_name, {'form': form})


class ContactFormView(View):
    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        logging(name, email, phone, message)  # Check the values in the console
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            phone_number=phone,
            body_message=message
        )

        return HttpResponse('Form submitted successfully!')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')

        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            body_message=message,
            phone_number=phone  
        ) 

        return HttpResponseRedirect(reverse('home'))


