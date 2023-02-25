from django.db import models
from django.urls import reverse


class Link(models.Model):
    short_url = models.SlugField(max_length=80, db_index=True, primary_key=True, verbose_name='Короткая ссылка')
    is_enabled = models.BooleanField(default=True, verbose_name='Включить ссылку')
    long_url = models.CharField(max_length=65535, verbose_name='Длинная ссылка')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_url

    def get_absolute_url(self):
        return reverse('link_edit', kwargs={'link_id': self.short_url})

    class Meta:
        verbose_name = 'Short URLs'
        verbose_name_plural = 'Short URLs'
        ordering = ['short_url']


class Click(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=65535, null=True)
