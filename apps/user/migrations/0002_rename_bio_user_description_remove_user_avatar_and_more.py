# Generated by Django 5.1 on 2024-08-08 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bio',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='profilephoto',
            field=models.ImageField(blank=True, null=True, upload_to='profilephotos/'),
        ),
    ]