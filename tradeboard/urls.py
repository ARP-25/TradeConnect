"""URL Configuration for TradeBoard Application"""

from django.urls import path
from . import views


urlpatterns = [
    # URL for submitting a form
    path("submit/", views.submit_form, name="submit_form"),
    # Homepage displaying a list of trade posts
    path("", views.TradePostList.as_view(), name="home"),
    # URL for creating a new trade post
    path("tradepostcreate/", views.TradePostCreate.as_view(), name="tradepost_create"),
    # URL for submitting a new trade post
    path(
        "tradepostcreatesubmit/",
        views.TradePostCreate.as_view(),
        name="tradepost_create_submit",
    ),
    # URL for displaying details of a trade post
    path("<slug:slug>/", views.TradePostDetail.as_view(), name="tradepost_detail"),
    # URL for rating a trade post
    path(
        "rating/<slug:slug>/", views.TradePostRating.as_view(), name="tradepost_rating"
    ),
    # URL for deleting a trade post
    path(
        "delete/<slug:slug>/", views.TradePostDelete.as_view(), name="tradepost_delete"
    ),
    # URL for editing a trade post
    path(
        "tradepost/edit/<slug:trade_post_slug>/",
        views.TradePostEdit.as_view(),
        name="tradepost_edit",
    ),
]
