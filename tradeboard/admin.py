from django.contrib import admin

from .models import TradePost, Rating, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(TradePost)
class TradePostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ("description",)
    list_filter = ('status', 'created_at')
    list_display = ('title', 'slug', 'status', 'created_at')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_at','approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, reqeust, queryset):
        queryset.update(approved=True)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'rating')
    list_filter = ('rating',)
    search_fields = ('post__title', 'user__username')

