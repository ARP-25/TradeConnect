from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]

class TradePost(models.Model):
    """
    Model representing a trade post.

    Attributes:
        title (str): The title of the trade post.
        slug (str): The slugified version of the title used in URLs.
        author (User): The author of the trade post.
        description (str): The description of the trade post.
        trade_image (CloudinaryField): The image associated with the trade post.
        created_at (DateTime): The date and time when the trade post was created.
        updated_at (DateTime): The date and time when the trade post was last updated.
        status (int): The status of the trade post (Draft or Published).

    Methods:
        average_rating: Calculate the average rating of the trade post based on ratings.

    Meta:
        ordering: Ordering of trade posts by creation date.
    """
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
    """
    Model representing a rating given to a trade post.

    Attributes:
        post (TradePost): The trade post associated with the rating.
        user (User): The user who rated the trade post.
        rating (int): The rating value given to the trade post.

    """
    post = models.ForeignKey(TradePost, on_delete=models.CASCADE,
        related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Comment(models.Model):
    """
    Model representing a comment on a trade post.

    Attributes:
        tradepost (TradePost): The trade post associated with the comment.
        name (str): The name of the commenter.
        email (str): The email of the commenter.
        body (str): The content of the comment.
        created_at (DateTime): The date and time when the comment was created.
        approved (bool): The approval status of the comment.

    Meta:
        ordering: Ordering of comments by creation date.
    """
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
    """
    Model representing a contact message.

    Attributes:
        name (str): The name of the person sending the message.
        email (str): The email of the person sending the message.
        phone_number (int): The phone number of the person sending the message.
        body_message (str): The content of the message.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    body_message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}- {self.phone_number}- {self.body_message}"


@receiver(pre_save, sender=TradePost)
def create_slug(sender, instance, *args, **kwargs):
    """
    Pre-save signal receiver to create a slug for a TradePost instance.

    Args:
        sender: The model class.
        instance: The instance being saved.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    if not instance.slug or instance.slug == '':
        instance.slug = slugify(instance.title)








