# Generated by Django 2.1.7 on 2020-01-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='메인노출여부'),
        ),
    ]
