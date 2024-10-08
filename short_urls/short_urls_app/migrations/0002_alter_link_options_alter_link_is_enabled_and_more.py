# Generated by Django 4.2 on 2024-10-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_urls_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['short_url'], 'verbose_name': 'Short URLs', 'verbose_name_plural': 'Short URLs'},
        ),
        migrations.AlterField(
            model_name='link',
            name='is_enabled',
            field=models.BooleanField(default=True, help_text='Выключенные ссылки не обрабатываются', verbose_name='Включить ссылку'),
        ),
        migrations.AlterField(
            model_name='link',
            name='long_url',
            field=models.CharField(max_length=65535, verbose_name='Длинная ссылка'),
        ),
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.SlugField(max_length=80, primary_key=True, serialize=False, verbose_name='Короткая ссылка'),
        ),
    ]
