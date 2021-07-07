from django.db import models


class BlogModel(models.Model):
    name = models.TextField(default='')
    image = models.FileField(upload_to='files/')
    description = models.TextField(default='')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
