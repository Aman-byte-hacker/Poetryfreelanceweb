# Generated by Django 3.1.5 on 2021-01-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.CharField(default='', max_length=200),
        ),
    ]