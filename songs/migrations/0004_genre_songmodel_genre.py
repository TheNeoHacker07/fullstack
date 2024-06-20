# Generated by Django 5.0.6 on 2024-06-20 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_alter_songmodel_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_genre', models.CharField(max_length=12, verbose_name='ЖАНР')),
            ],
        ),
        migrations.AddField(
            model_name='songmodel',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre', to='songs.genre'),
        ),
    ]