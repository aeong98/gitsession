# Generated by Django 3.1.7 on 2021-04-01 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='writer',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
