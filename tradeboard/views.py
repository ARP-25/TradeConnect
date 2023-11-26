from django.shortcuts import render
from django.views import generic
from .models import TradePost


# Create your views here.
class TradePostList(generic.ListView):
    model = TradePost
    queryset = TradePost.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'
    paginate_by = 6
