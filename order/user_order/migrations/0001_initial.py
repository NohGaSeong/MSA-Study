# Generated by Django 4.2.1 on 2023-05-30 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shpo_name', models.CharField(max_length=20)),
                ('shop_address', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_data', models.DateTimeField(verbose_name='data ordered')),
                ('address', models.CharField(max_length=40)),
                ('deliver_finish', models.BooleanField(default=0)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_order.shop')),
            ],
        ),
    ]
