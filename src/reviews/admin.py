from django.contrib import admin

from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    fields = ['media', 'title', 'body', 'verdict']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    list_display = ['author', 'media', 'title', 'verdict', 'created', 'last_modified']


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    exclude = ['created', 'last_modified']
    list_display = ['title', 'release', 'verdict', 'publisher', 'last_modified']


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    exclude = ['created', 'last_modified']
    list_display = ['name', 'last_modified']


admin.site.register(models.Category)