from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.generic import DeleteView, TemplateView
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg
from .models import TradePost, Rating, ContactMessage, Comment
from .forms import CommentForm, TradePostForm



class TradePostList(generic.ListView):
    """
    ListView to display a paginated list of trade posts based on certain criteria.

    Attributes:
        model (Model): The model class used for this ListView.
        template_name (str): The HTML template used for rendering the list.
        paginate_by (int): Number of items to display per page.

    Methods:
        get_queryset: Retrieve the queryset based on filters and sorting criteria.
    """

    model = TradePost
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Retrieve the queryset based on sorting criteria.

        Returns:
            queryset: Filtered and sorted queryset of TradePost objects.
        """
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
    """
    View to display the details of a specific trade post and handle comments.

    Methods:
        get: Handle GET requests for viewing trade post details.
        post: Handle POST requests for adding comments to a trade post.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Handle GET requests to display trade post details and approved comments.

        Args:
            request (HttpRequest): The request object.
            slug (str): The slug of the trade post.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: Rendered HTML template displaying trade post details and comments.
        """
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
        """
        Handle POST requests to add comments to a trade post.

        Args:
            request (HttpRequest): The request object.
            slug (str): The slug of the trade post.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: Rendered HTML template with comment addition status.
        """
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
    """
    View to handle user ratings for trade posts.

    Methods:
        post: Handle POST requests to add or update ratings for a trade post.
    """
    def post(self, request, slug):
        """
        Handle POST requests to add or update ratings for a trade post.

        Args:
            request (HttpRequest): The request object.
            slug (str): The slug of the trade post.

        Returns:
            HttpResponseRedirect: Redirects back to the trade post detail page.
        """
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
    """
    View to handle the deletion of a trade post.

    Methods:
        post: Handle POST requests to delete a trade post.
    """
    def post(self, request, slug):
        """
        Handle POST requests to delete a trade post.

        Args:
            request (HttpRequest): The request object.
            slug (str): The slug of the trade post.

        Returns:
            HttpResponseRedirect: Redirects to the previous page or home upon deletion.
        """
        tradepost = get_object_or_404(TradePost, slug=slug)

        try:
            tradepost.delete()
            messages.success(request, 'Trade Post has been deleted!')
        except Exception as e:
            messages.error(request, f"Error deleting Trade Post: {e}")
                

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))


class TradePostCreate(View):
    """
    View to handle the creation of new trade posts.

    Attributes:
        template_name (str): The HTML template used for creating a new trade post.

    Methods:
        get: Handle GET requests to display the trade post creation form.
        post: Handle POST requests to create a new trade post.
    """

    template_name = 'tradepost_create.html'

    def get(self, request):
        """
        Handle GET requests to display the trade post creation form.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Rendered HTML template with the trade post creation form.
        """
        form = TradePostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Handle POST requests to create a new trade post.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponseRedirect: Redirects to the home page upon successful creation or renders the form with errors.
        """
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
    """
    View to handle the editing of a trade post.

    Attributes:
        template_name (str): The HTML template used for editing a trade post.

    Methods:
        get: Handle GET requests to display the trade post edit form.
        post: Handle POST requests to update a trade post.
    """

    template_name = 'tradepost_edit.html'  

    def get(self, request, trade_post_slug):  
        """
        Handle GET requests to display the trade post edit form.

        Args:
            request (HttpRequest): The request object.
            trade_post_slug (str): The slug of the trade post to be edited.

        Returns:
            HttpResponse: Rendered HTML template with the trade post edit form and trade post details.
        """
        trade_post = get_object_or_404(TradePost, slug=trade_post_slug)
        form = TradePostForm(instance=trade_post)
        return render(request, self.template_name, {'form': form,'trade_post': trade_post})

    def post(self, request, trade_post_slug):  
        """
        Handle POST requests to update a trade post.

        Args:
            request (HttpRequest): The request object.
            trade_post_slug (str): The slug of the trade post to be updated.

        Returns:
            HttpResponseRedirect: Redirects to the home page upon successful update or renders the form with errors.
        """
        trade_post = get_object_or_404(TradePost, slug=trade_post_slug)
        form = TradePostForm(request.POST, instance=trade_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited a TradePost.')
            return HttpResponseRedirect(reverse('home'))  
        return render(request, self.template_name, {'form': form})


def submit_form(request):
    """
    Handle form submission for contact messages.

    Args:
        request (HttpRequest): The request object containing form data.

    Returns:
        HttpResponseRedirect: Redirects to the home page upon successful form submission.
    """
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
        messages.success(request, 'Thank you for submitting a Message.')
        return HttpResponseRedirect(reverse('home'))


