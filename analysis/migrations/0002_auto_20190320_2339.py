# Generated by Django 2.1.4 on 2019-03-20 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]