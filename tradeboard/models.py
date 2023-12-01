from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]

class TradePost(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    trade_image = CloudinaryField("image",default="placeholder")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            total_ratings = sum([rating.rating for rating in ratings])
            return total_ratings / len(ratings)
        return 0  


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

    class Meta:
        ordering = ["created_at"]
    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    body_message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}- {self.phone_number}- {self.body_message}"


@receiver(pre_save, sender=TradePost)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug or instance.slug == '':
        instance.slug = slugify(instance.title)








