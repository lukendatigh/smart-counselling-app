# Generated by Django 2.1.4 on 2019-02-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellia', '0002_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='counsellee_archived',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='counsellor_archived',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='archived',
            field=models.BooleanField(default=False, null=True),
        ),
    ]