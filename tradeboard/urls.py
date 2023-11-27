from . import views
from django.urls import path

urlpatterns = [
    path("", views.TradePostList.as_view(), name="home"),
    path("<slug:slug>/", views.TradePostDetail.as_view(), name="tradepost_detail"),
    path('rating/<slug:slug>/', views.TradePostRating.as_view(), name='tradepost_rating'),
]