from django.db import models

class Library(models.Model):
    slug = models.SlugField(primary_key = True)
    name = models.CharField(max_length = 50)
    short_desc = models.CharField(max_length = 500)
    long_desc = models.TextField()
    url = models.URLField(verify_exists = False)
    current_version = models.CharField(max_length = 20)
    mimetype = models.CharField(max_length = 50)

    def get_absolute_url(self):
        return "/library/%s/" % self.slug

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Libraries"

class Version(models.Model):
    library = models.ForeignKey("Library")
    version = models.CharField(max_length = 20)
    data = models.TextField()
    compressed = models.BooleanField(default = True)
    dependencies = models.ManyToManyField("Dependency", blank = True, null = True)

    def get_absolute_url(self):
        if self.version == self.library.current_version:
            return "/%s" % self.library.slug
        else: 
            return "/%s/%s" % (self.library.slug, self.version)

    def __unicode__(self):
        return "%s: version %s" % (self.library.name, self.version)

class Dependency(models.Model):
    library = models.ForeignKey("Library")
    min_version = models.CharField(max_length = 20)

    class Meta:
        verbose_name_plural = "Dependencies"
