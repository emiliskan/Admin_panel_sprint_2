# Generated by Django 3.1 on 2021-05-07 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20210505_1318'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personmedia',
            unique_together={('person', 'film', 'person_type')},
        ),
    ]
