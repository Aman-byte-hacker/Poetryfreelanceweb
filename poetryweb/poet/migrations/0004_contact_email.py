# Generated by Django 3.1.5 on 2021-01-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
