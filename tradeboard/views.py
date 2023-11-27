from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import TradePost
from .forms import CommentForm

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
        rated = False 
        if tradepost.ratings.filter(id=self.request.user.id).exists():
            rated = True

        return render(
            request,
            "tradepost_detail.html",
            {
                "tradepost": tradepost, "comments": comments,"commented": False, "rated": rated, "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = TradePost.objects.filter(status=1)
        tradepost = get_object_or_404(queryset, slug=slug)
        comments = tradepost.comments.filter(approved=True).order_by('created_at')
        rated = False 
        if tradepost.ratings.filter(id=self.request.user.id).exists():
            rated = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.tradepost = tradepost
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "tradepost_detail.html",
            {
                "tradepost": tradepost, "comments": comments,"commented": True, "rated": rated, "comment_form": CommentForm()
            },
        )

