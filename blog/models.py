from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_author')
    content = models.TextField()
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='article_group')

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title