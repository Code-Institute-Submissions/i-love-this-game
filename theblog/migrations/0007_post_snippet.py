# Generated by Django 3.2 on 2022-08-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the link above to read the blog post', max_length=255),
        ),
    ]
