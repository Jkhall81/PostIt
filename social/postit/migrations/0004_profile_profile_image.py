# Generated by Django 4.2.2 on 2023-06-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
