# Generated by Django 3.1 on 2021-05-01 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_auto_20210430_2042"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="personmedia",
            unique_together={("person", "film")},
        ),
    ]