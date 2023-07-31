# Generated by Django 4.1.6 on 2023-07-31 09:14

from django.db import migrations, models
import ezypzy.models


class Migration(migrations.Migration):

    dependencies = [
        ('ezypzy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetable',
            name='file',
            field=models.FileField(storage=ezypzy.models.S3MediaStorage(), upload_to='documents/'),
        ),
    ]
