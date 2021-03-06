# Generated by Django 2.0.7 on 2018-07-30 18:46

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('titleru', models.CharField(default=None, max_length=200)),
                ('preview_image', models.ImageField(default=None, null=True, upload_to='media/previews')),
                ('short_text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, default='')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Статья сайта',
                'verbose_name_plural': 'Статьи сайта',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=64, unique=True, verbose_name='Имя категории')),
                ('slug_category', models.SlugField(blank=True, default='', max_length=64, unique=True, verbose_name='Транслит')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория статьи',
                'verbose_name_plural': 'Категории статей',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название тэга')),
                ('slug_tag', models.SlugField(blank=True, default='', max_length=64, unique=True, verbose_name='Транслит')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Тэг статьи',
                'verbose_name_plural': 'Тэги статей',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.ArticleCategory'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.ArticleTag', verbose_name='Тэги'),
        ),
    ]
