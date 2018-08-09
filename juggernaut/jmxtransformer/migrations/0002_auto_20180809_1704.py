# Generated by Django 2.1 on 2018-08-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jmxtransformer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jmx',
            name='date_updated',
            field=models.DateTimeField(null=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='jmx',
            name='updated_jmxfile',
            field=models.FileField(null=True, upload_to='jmxes/uploaded'),
        ),
        migrations.AlterField(
            model_name='jmx',
            name='date_added',
            field=models.DateTimeField(auto_now=True, verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='jmx',
            name='jmxfile',
            field=models.FileField(upload_to='jmxes/uploaded'),
        ),
    ]