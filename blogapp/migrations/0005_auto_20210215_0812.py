# Generated by Django 3.1.6 on 2021-02-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='image/'),
        ),
    ]
