# Generated by Django 4.2.1 on 2023-05-30 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='shpo_name',
            new_name='shop_name',
        ),
    ]