"""
Module containing Django forms for comments and trade posts.

Includes forms:
- CommentForm: Form for adding a comment.
- TradePostForm: Form for creating or updating a trade post.
"""
from django import forms
from .models import Comment, TradePost



class CommentForm(forms.ModelForm):
    """
    Form for adding a comment.

    Fields:
        body (str): The content of the comment.

    """

    class Meta:
        """
        Form for adding a comment.

        Fields:
            body (str): The content of the comment.
        """
        model = Comment
        fields = ("body",)

    body = forms.CharField(label="", widget=forms.Textarea)


class TradePostForm(forms.ModelForm):
    """
    Form for creating or updating a trade post.

    Fields:
        title (str): The title of the trade post.
        description (str): The description of the trade post.
        trade_image (ImageField): The image associated with the trade post.

    """

    class Meta:
        model = TradePost
        fields = ["title", "description", "trade_image"]

    trade_image = forms.ImageField()
