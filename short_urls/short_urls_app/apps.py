from django.apps import AppConfig


class ShortUrlsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'short_urls_app'
    verbose_name = 'Short URLs'  # App name in admin panel
