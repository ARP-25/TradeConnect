from . import views
from django.urls import path

urlpatterns = [
    path("", views.TradePostList.as_view(), name="home"),
]