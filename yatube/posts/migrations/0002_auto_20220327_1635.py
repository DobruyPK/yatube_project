# Generated by Django 2.2.19 on 2022-03-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]