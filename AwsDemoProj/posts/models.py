from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    # This line defines a Django model named Post. It inherits from models.Model, indicating that it's a Django model.
    post_title = models.CharField(max_length=255)
    post_description = models.TextField()
    post_shortname = models.SlugField(max_length=300, unique=True)
    post_published_datetime = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)