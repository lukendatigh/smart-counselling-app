# Generated by Django 2.1.4 on 2019-02-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190220_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellee',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to='profile_photos'),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to='profile_photos'),
        ),
    ]
