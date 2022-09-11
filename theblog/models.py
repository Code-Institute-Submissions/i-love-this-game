from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    """
    Profile model
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = CloudinaryField(
        'image', null=True, blank=True, folder="media/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=255)
    header_image = CloudinaryField(
        'image', null=True, blank=True, folder="media/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=False, null=False)
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    """
    Comment model
    """
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author.username)


class Contact(models.Model):
    """
    Contact model
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contacts")
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"{self.subject} - {self.author.username}"
