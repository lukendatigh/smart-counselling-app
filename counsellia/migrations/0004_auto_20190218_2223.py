# Generated by Django 2.1.4 on 2019-02-18 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsellia', '0003_auto_20190218_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]