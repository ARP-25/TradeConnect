"""
Admin configurations for managing TradePost, Comment,
Rating, and ContactMessage models in the Django admin interface.

Provides customizations for the display, filtering,
and actions available in the admin view for each model.
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TradePost, Rating, Comment, ContactMessage



@admin.register(TradePost)
class TradePostAdmin(SummernoteModelAdmin):
    """
    Admin view for TradePost model.

    Attributes:
        prepopulated_fields (dict): Automatically populate slug field using the title.
        summernote_fields (list): Fields to be rendered using Summernote.
        list_filter (tuple): Filters available in the admin list view.
        list_display (tuple): Fields displayed in the admin list view.
        search_fields (list): Fields searchable in the admin interface.
    """

    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)
    list_filter = ("status", "created_at")
    list_display = ("title", "slug", "status", "created_at")
    search_fields = ["title", "content"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin view for Comment model.

    Attributes:
        list_display (tuple): Fields displayed in the admin list view.
        list_filter (tuple): Filters available in the admin list view.
        search_fields (tuple): Fields searchable in the admin interface.
        actions (list): Available actions for selected comments.
    """

    list_display = ("name", "body", "created_at", "approved")
    list_filter = ("approved", "created_at")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, queryset):
        """
        Action to approve selected comments.

        Marks the selected comments as approved.

        Args:
            request: The request object.
            queryset: A queryset containing the selected comments.
        """
        queryset.update(approved=True)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Admin view for Rating model.

    Attributes:
        list_display (tuple): Fields displayed in the admin list view.
        list_filter (tuple): Filters available in the admin list view.
        search_fields (tuple): Fields searchable in the admin interface.
    """

    list_display = ("post", "user", "rating")
    list_filter = ("rating",)
    search_fields = ("post__title", "user__username")


@admin.register(ContactMessage)
class MessageAdmin(admin.ModelAdmin):
    """
    Admin view for ContactMessage model.

    Attributes:
        list_display (tuple): Fields displayed in the admin list view.
    """

    list_display = ("name", "email", "phone_number", "body_message")
