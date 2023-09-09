from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    wikipedia = models.URLField(blank=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, default=0)
    summary = models.TextField(blank=True, default="RAS")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    # @property
    # def publish_string(self):
    #     if self.published:
    #         return "L'article publié"
    #     return "L'article est inaccessible"
