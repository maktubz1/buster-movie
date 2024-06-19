# Generated by Django 5.0.6 on 2024-05-14 22:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('duration', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('rating', models.CharField(choices=[('G', 'G'), ('PG', 'Pg'), ('PG-13', 'Pg 13'), ('R', 'R'), ('NC-17', 'Nc 17')], default='G', max_length=20)),
                ('synopsis', models.TextField(blank=True, default='', null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
