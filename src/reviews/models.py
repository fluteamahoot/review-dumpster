from django.db import models
from django.conf import settings

from ckeditor.fields import RichTextField


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)


class Media(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher)

    release = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def verdict(self):
        return "%s%%" % (self.review_set.aggregate(models.Avg('verdict'))['verdict__avg'])

    def __str__(self):
        return "%s (%s)" % (self.title, self.release)


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    media = models.ForeignKey(Media)

    title = models.CharField(max_length=255)
    body = RichTextField()
    verdict = models.IntegerField(default=0, choices=(
        (100, 'Yay'),
        (50, 'Meh'),
        (0, 'Nah'),
    ))

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%s] %s <%s>" % (self.media, self.title, self.author.name)
