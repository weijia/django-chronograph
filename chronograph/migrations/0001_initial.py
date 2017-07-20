# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('frequency', models.CharField(max_length=10, verbose_name='frequency', choices=[(b'YEARLY', 'Yearly'), (b'MONTHLY', 'Monthly'), (b'WEEKLY', 'Weekly'), (b'DAILY', 'Daily'), (b'HOURLY', 'Hourly'), (b'MINUTELY', 'Minutely'), (b'SECONDLY', 'Secondly')])),
                ('params', models.TextField(help_text='Comma-separated list of <a href="http://labix.org/python-dateutil" target="_blank">rrule parameters</a>. e.g: interval:15', null=True, verbose_name='params', blank=True)),
                ('command', models.CharField(help_text='A valid django-admin command to run.', max_length=200, verbose_name='command', blank=True)),
                ('args', models.CharField(help_text='Space separated list; e.g: arg1 option1=True', max_length=200, verbose_name='args', blank=True)),
                ('disabled', models.BooleanField(default=False, help_text='If checked this job will never run.')),
                ('next_run', models.DateTimeField(help_text="If you don't set this it will be determined automatically", null=True, verbose_name='next run', blank=True)),
                ('last_run', models.DateTimeField(verbose_name='last run', null=True, editable=False, blank=True)),
                ('is_running', models.BooleanField(default=False, editable=False)),
                ('last_run_successful', models.BooleanField(default=True, editable=False)),
                ('lock_file', models.CharField(max_length=255, editable=False, blank=True)),
                ('force_run', models.BooleanField(default=False)),
                ('subscribers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ('disabled', 'next_run'),
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_date', models.DateTimeField(auto_now_add=True)),
                ('stdout', models.TextField(blank=True)),
                ('stderr', models.TextField(blank=True)),
                ('success', models.BooleanField(default=True, editable=False)),
                ('duration', models.FloatField(editable=False)),
                ('job', models.ForeignKey(to='chronograph.Job')),
            ],
            options={
                'ordering': ('-run_date',),
            },
        ),
    ]
