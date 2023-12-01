from . import views
from django.urls import path

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
    path('', views.TradePostList.as_view(), name='home'),
    path('tradepostcreate/', views.TradePostCreate.as_view(), name='tradepost_create'),
    path('tradepostcreatesubmit/', views.TradePostCreate.as_view(), name='tradepost_create_submit'),
    path('<slug:slug>/', views.TradePostDetail.as_view(), name='tradepost_detail'),
    path('rating/<slug:slug>/', views.TradePostRating.as_view(), name='tradepost_rating'),
    path('delete/<slug:slug>/', views.TradePostDelete.as_view(), name='tradepost_delete'),
    path('tradepost/edit/<slug:trade_post_slug>/', views.TradePostEdit.as_view(), name='tradepost_edit'),

    
]