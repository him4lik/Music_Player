# Generated by Django 3.2 on 2021-07-22 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_alter_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='is_public',
        ),
    ]