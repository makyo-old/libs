from django.db import models

class Library(models.Model):
    slug = models.SlugField(primary_key = True)
    name = models.CharField(max_length = 50)
    short_desc = models.CharField(max_length = 500)
    long_desc = models.TextField()
    url = models.URLField(verify_exists = False)
    current_version = models.CharField(max_length = 20)
    mime_type = models.CharField(max_length = 50)

class Version(models.Model):
    version = models.CharField(max_length = 20)
    data = models.TextField()
    compressed = models.BooleanField(default = True)
