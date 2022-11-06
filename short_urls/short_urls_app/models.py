from django.db import models


class Link(models.Model):
    short_url = models.SlugField(max_length=80, primary_key=True)
    is_enabled = models.BooleanField(default=True)
    long_url = models.CharField(max_length=65535)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Click(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=65535, null=True)
