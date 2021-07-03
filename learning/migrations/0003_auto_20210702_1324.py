# Generated by Django 3.2.4 on 2021-07-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_blogcommentmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCommentModel',
        ),
        migrations.AddField(
            model_name='blogimagemodel',
            name='date_comment',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blogimagemodel',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blogvideosmodel',
            name='date_comment',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blogvideosmodel',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
