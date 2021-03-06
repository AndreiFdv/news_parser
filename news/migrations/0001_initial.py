# Generated by Django 3.2.9 on 2021-12-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(blank=True)),
                ('author', models.CharField(blank=True, max_length=500)),
                ('content', models.TextField(blank=True, null=True)),
                ('short_text', models.TextField(blank=True, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000)),
                ('img', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=500, unique=True)),
                ('user_name', models.CharField(max_length=500)),
            ],
        ),
    ]
