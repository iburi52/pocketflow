# Generated by Django 3.1 on 2020-10-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_api', '0002_auth0user'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='created_by',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
