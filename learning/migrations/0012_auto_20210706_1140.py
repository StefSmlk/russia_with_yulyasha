# Generated by Django 3.2.4 on 2021-07-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0011_auto_20210706_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimagemodel',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
