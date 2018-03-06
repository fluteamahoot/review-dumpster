from django.db import models
from django.conf import settings

from ckeditor.fields import RichTextField


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Media(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher)

    release = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    media = models.ForeignKey(Media)

    title = models.CharField(max_length=255)
    body = RichTextField()
    verdict = models.IntegerField(default=0, choices=(
        (1, 'Yay'),
        (0, 'Meh'),
        (-1, 'Nah'),
    ))

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)