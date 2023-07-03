from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    author = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog_post_detail", args=[self.slug])

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)
        
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
