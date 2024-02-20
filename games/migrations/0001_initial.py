# Generated by Django 5.0.1 on 2024-02-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('released_date', models.DateField()),
                ('character', models.TextField()),
                ('preview_image', models.ImageField(upload_to='game_preview_image/')),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('triller_url', models.CharField(blank=True, max_length=100, null=True)),
                ('downloaded', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='game_torrent_file/')),
                ('gener', models.CharField(max_length=100)),
            ],
        ),
    ]