# Generated by Django 2.2.19 on 2022-03-27 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20220327_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
    ]