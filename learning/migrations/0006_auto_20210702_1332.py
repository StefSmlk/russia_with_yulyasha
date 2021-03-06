# Generated by Django 3.2.4 on 2021-07-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_auto_20210702_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimagemodel',
            name='date',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='date',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='image',
            field=models.FileField(upload_to='files'),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
