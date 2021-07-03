from django.contrib import admin

# Register your models here.
from learning.models import BlogVideosModel, BlogImageModel, ImageCommentsModel

admin.site.register(BlogImageModel)
admin.site.register(BlogVideosModel)
admin.site.register(ImageCommentsModel)
