# Generated by Django 5.1.5 on 2025-01-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='is_allowed',
            field=models.BooleanField(default=True, verbose_name='Access allowed'),
        ),
    ]
