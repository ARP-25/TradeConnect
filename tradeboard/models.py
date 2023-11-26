from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]

class TradePost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    trade_image = CloudinaryField("image",default="placeholder")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    #sortiert posts von neu zu alt
    class Meta:
        ordering = ['-created_at']
    #tostring
    def __str__(self):
        return self.title
    #avrgrating ausgabe
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            total_ratings = sum([rating.rating for rating in ratings])
            return total_ratings / len(ratings)
        return 0  # Default if no ratings


class Rating(models.Model):
    post = models.ForeignKey(TradePost, on_delete=models.CASCADE,
        related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Comment(models.Model):
    tradepost = models.ForeignKey(TradePost, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    #oldest comments listed first
    class Meta:
        ordering = ["created_at"]
    #tostring
    def __str__(self):
        return f"Comment {self.body} by {self.name}"



