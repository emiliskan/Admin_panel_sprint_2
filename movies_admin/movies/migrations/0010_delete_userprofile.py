# Generated by Django 3.1 on 2021-05-02 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_media_genres'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
