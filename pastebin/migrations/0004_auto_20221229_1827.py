# Generated by Django 3.2.16 on 2022-12-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0003_rename_texted_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.CharField(default='No text was entered', max_length=10000),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(default='No title was entered', max_length=64),
        ),
    ]