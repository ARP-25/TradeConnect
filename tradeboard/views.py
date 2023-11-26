from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import TradePost


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
                "tradepost": tradepost, "comments": comments, "rated": rated
            },
        )


