# Generated by Django 3.2.4 on 2021-07-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0013_auto_20210706_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
