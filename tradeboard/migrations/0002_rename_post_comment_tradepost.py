# Generated by Django 4.2.7 on 2023-11-25 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradeboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='tradepost',
        ),
    ]