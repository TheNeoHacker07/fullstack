# Generated by Django 5.0.6 on 2024-06-25 19:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0004_alter_usercabinet_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercabinet',
            name='author',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cabinet', to=settings.AUTH_USER_MODEL, verbose_name='пользаватель'),
        ),
    ]