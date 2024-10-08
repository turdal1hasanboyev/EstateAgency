# Generated by Django 4.2.14 on 2024-09-01 08:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('slug', models.SlugField(blank=True, max_length=225, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='agents/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=225, null=True, unique=True)),
                ('email_2', models.EmailField(blank=True, max_length=225, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=225, null=True)),
                ('skype', models.CharField(blank=True, max_length=225, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
