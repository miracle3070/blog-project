# Generated by Django 3.1.6 on 2021-02-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20210214_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
