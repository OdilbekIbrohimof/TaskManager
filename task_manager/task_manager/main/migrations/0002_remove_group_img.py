# Generated by Django 3.2 on 2023-04-18 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='img',
        ),
    ]