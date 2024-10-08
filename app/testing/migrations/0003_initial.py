# Generated by Django 5.0.7 on 2024-09-07 06:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testing', '0002_delete_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='タイトル')),
                ('code', models.TextField(blank=True, verbose_name='コード')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='本文')),
                ('commented_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.snippet', verbose_name='スニペット')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='タグ')),
                ('snippets', models.ManyToManyField(related_name='tags', related_query_name='tag', to='testing.snippet')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
    ]
