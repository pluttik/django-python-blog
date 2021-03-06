# Generated by Django 3.2 on 2021-05-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
                ('code', models.TextField()),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
