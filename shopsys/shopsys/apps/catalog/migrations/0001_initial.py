# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('slug', models.SlugField(help_text=b'\xe6\xa0\xb9\xe6\x8d\xaename\xe7\x94\x9f\xe6\x88\x90\xe7\x9a\x84\xef\xbc\x8c\xe7\x94\xa8\xe4\xba\x8e\xe7\x94\x9f\xe6\x88\x90\xe9\xa1\xb5\xe9\x9d\xa2URL, \xe5\xbf\x85\xe9\xa1\xbb\xe5\x94\xaf\xe4\xb8\x80', unique=True, verbose_name=b'slug')),
                ('description', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\xbf\x80\xe6\xb4\xbb')),
                ('meta_keywords', models.CharField(help_text=b'Meta\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97\xef\xbc\x8c\xe6\x9c\x89\xe5\x88\xa9\xe4\xba\x8eSEO\xef\xbc\x8c\xe7\x94\xa8\xe9\x80\x97\xe5\x8f\xb7\xe5\x88\x86\xe9\x9a\x94', max_length=255, verbose_name=b'Meta \xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('meta_description', models.CharField(help_text=b'Meta\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255, verbose_name=b'Meta\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-create_at'],
                'db_table': 'categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('slug', models.SlugField(help_text=b'\xe6\xa0\xb9\xe6\x8d\xaename\xe7\x94\x9f\xe6\x88\x90\xe7\x9a\x84\xef\xbc\x8c\xe7\x94\xa8\xe4\xba\x8e\xe7\x94\x9f\xe6\x88\x90\xe9\xa1\xb5\xe9\x9d\xa2URL, \xe5\xbf\x85\xe9\xa1\xbb\xe5\x94\xaf\xe4\xb8\x80', unique=True, verbose_name=b'slug')),
                ('brand', models.CharField(max_length=50, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('sku', models.CharField(max_length=50, verbose_name=b'\xe8\xae\xa1\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d')),
                ('price', models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(default=0.0, verbose_name=b'\xe6\x97\xa7\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=9, decimal_places=2, blank=True)),
                ('image', models.ImageField(upload_to=b'', max_length=50, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\xbf\x80\xe6\xb4\xbb')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name=b'\xe6\xa0\x87\xe4\xb8\xba\xe7\x95\x85\xe9\x94\x80')),
                ('is_featured', models.BooleanField(default=False, verbose_name=b'\xe6\xa0\x87\xe4\xb8\xba\xe6\x8e\xa8\xe8\x8d\x90')),
                ('quantity', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('description', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('meta_keywords', models.CharField(help_text=b'Meta\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97\xef\xbc\x8c\xe6\x9c\x89\xe5\x88\xa9\xe4\xba\x8eSEO\xef\xbc\x8c\xe7\x94\xa8\xe9\x80\x97\xe5\x8f\xb7\xe5\x88\x86\xe9\x9a\x94', max_length=255, verbose_name=b'Meta \xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('meta_description', models.CharField(help_text=b'Meta\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255, verbose_name=b'Meta\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'ordering': ['-create_at'],
                'db_table': 'products',
            },
        ),
    ]
