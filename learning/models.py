from django.db import models


# Create your models here.

class BlogVideosModel(models.Model):
    name = models.TextField(max_length=100)
    image = models.FileField(upload_to='files')
    description = models.TextField(max_length=200)
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.name


class BlogImageModel(models.Model):
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=200)
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.name


class ImageCommentsModel(models.Model):
    image_id = models.TextField(default='')
    text = models.TextField()
    date_comment = models.DateField(auto_now=True)


class VideoCommentsModel(models.Model):
    video_id = models.TextField(default='')
    text = models.TextField()
    date_comment = models.DateField(auto_now=True)
