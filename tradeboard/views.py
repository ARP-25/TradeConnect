from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView
from .models import TradePost, Rating
from .forms import CommentForm
import logging


# Create your views here.
class TradePostList(generic.ListView):
    model = TradePost
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        return TradePost.objects.filter(status=1).order_by('-created_at')


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


