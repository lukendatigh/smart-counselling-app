# Generated by Django 2.1.4 on 2019-02-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190206_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsellee',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='counsellor',
            name='available',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
