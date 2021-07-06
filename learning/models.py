from django.db import models


class BlogVideosModel(models.Model):
    name = models.TextField(default='')
    image = models.FileField(upload_to='files/')
    description = models.TextField(default='')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class BlogImageModel(models.Model):
    name = models.TextField(default='')
    image = models.ImageField(upload_to='images/')
    description = models.TextField(default='')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class ImageCommentsModel(models.Model):
    image_id = models.TextField(default='')
    text = models.TextField(verbose_name='')
    date_comment = models.DateField(auto_now=True)


class VideoCommentsModel(models.Model):
    video_id = models.TextField(default='')
    text = models.TextField(verbose_name='')
    date_comment = models.DateField(auto_now=True)
