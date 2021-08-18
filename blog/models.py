import os
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return self.title


def path_and_rename(instance, filename):
    upload_to = 'upload'
    ext = filename.split('.')[-1]

    random_id = uuid4().hex
    filename = f'{random_id}.{ext}'

    return os.path.join(upload_to, filename)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status='published')


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

    show_slider = models.BooleanField(default=False)
    visit = models.IntegerField(default=0)
    images = models.FileField(upload_to=path_and_rename, null=True, default='upload/fff.png')

    # default manager
    objects = models.Manager()

    # custom manager that return published post
    published = ArticleManager()

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title


class Contact(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)