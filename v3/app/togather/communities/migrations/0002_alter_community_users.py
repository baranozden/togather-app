# Generated by Django 4.2.7 on 2024-01-02 01:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='users',
            field=models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
