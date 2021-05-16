from django.db import models

class Post(models.Model):
    title         = models.CharField(max_length=120)
    slug          = models.SlugField(blank=True, unique=True)
    content       = models.TextField()
    code          = models.TextField()
    image         = models.ImageField(upload_to='blog_images/')
    timestamp     = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.slug
