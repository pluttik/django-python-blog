from django.db import models

class Tag(models.Model):
    name          = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title         = models.CharField(max_length=120)
    slug          = models.SlugField(unique=True)
    content       = models.TextField()
    code          = models.TextField(blank=True)
    image         = models.ImageField(blank=True, upload_to='blog_images/')
    timestamp     = models.DateTimeField(auto_now_add=False)
    tags          = models.ManyToManyField(Tag)

    def __str__(self):
        return self.slug
