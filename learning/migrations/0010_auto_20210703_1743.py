# Generated by Django 3.2.4 on 2021-07-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0009_rename_image_id_videocommentsmodel_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecommentsmodel',
            name='image_id',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='videocommentsmodel',
            name='video_id',
            field=models.TextField(default=''),
        ),
    ]
