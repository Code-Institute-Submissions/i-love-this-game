# Generated by Django 3.2 on 2022-08-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='80s & 90s NBA Blog', max_length=255),
        ),
    ]
