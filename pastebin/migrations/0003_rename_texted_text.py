# Generated by Django 3.2.16 on 2022-12-24 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0002_auto_20221224_2220'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Texted',
            new_name='Text',
        ),
    ]