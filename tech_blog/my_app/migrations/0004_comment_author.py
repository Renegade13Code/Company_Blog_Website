# Generated by Django 3.2.9 on 2021-12-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20211206_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.TextField(default='default', max_length=256),
            preserve_default=False,
        ),
    ]
