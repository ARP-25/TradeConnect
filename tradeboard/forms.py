from .models import Comment, TradePost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('body',)
    body = forms.CharField(label='', widget=forms.Textarea)


class TradePostForm(forms.ModelForm):
    class Meta:
        model = TradePost
        fields = ['title', 'description', 'trade_image']

    trade_image = forms.ImageField()





