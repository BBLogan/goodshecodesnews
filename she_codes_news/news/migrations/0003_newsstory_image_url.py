# Generated by Django 4.2.2 on 2023-12-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsstory_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]