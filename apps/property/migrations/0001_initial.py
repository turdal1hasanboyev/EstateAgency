# Generated by Django 5.1 on 2024-08-08 10:41

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('slug', models.SlugField(blank=True, max_length=225, null=True, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=225, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='properties/')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('type', models.CharField(blank=True, max_length=225, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'in_the_living'), (1, 'sale'), (2, 'rent')], default=None, null=True)),
                ('area', models.IntegerField(blank=True, default=0, null=True)),
                ('beds', models.IntegerField(blank=True, default=0, null=True)),
                ('boths', models.IntegerField(blank=True, default=0, null=True)),
                ('garage', models.IntegerField(blank=True, default=0, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.agent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]