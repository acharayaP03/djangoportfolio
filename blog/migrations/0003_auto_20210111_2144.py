# Generated by Django 3.1.4 on 2021-01-11 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210111_2143'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='Blog',
        ),
    ]
