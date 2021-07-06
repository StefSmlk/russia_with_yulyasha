# Generated by Django 3.2.4 on 2021-07-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0010_auto_20210703_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimagemodel',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogvideosmodel',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='imagecommentsmodel',
            name='text',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='videocommentsmodel',
            name='text',
            field=models.TextField(verbose_name=''),
        ),
    ]
