from django.db import models


class BlogSetting(models.Model):
    brand_name = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    bio = models.TextField()
    github = models.URLField(null=True, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.body


