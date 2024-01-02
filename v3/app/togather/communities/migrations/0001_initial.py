# Generated by Django 4.2.7 on 2024-01-02 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('task_type', models.CharField(choices=[('manual', 'Manual'), ('automated', 'Automated')], default='manual', max_length=9)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=6)),
                ('detailed_info', models.CharField(blank=True, max_length=128)),
                ('place', models.CharField(blank=True, max_length=64)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='togather/uploads/')),
                ('reminder', models.CharField(choices=[('none', 'None'), ('before_15', '15 minutes before'), ('before_30', '30 minutes before'), ('before_1d', '1 Day before')], default='none', max_length=17)),
                ('recurrence', models.CharField(choices=[('none', 'None'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='none', max_length=7)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.community')),
            ],
        ),
    ]
