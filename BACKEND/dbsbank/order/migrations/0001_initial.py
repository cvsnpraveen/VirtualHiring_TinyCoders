# Generated by Django 4.0.1 on 2022-01-29 06:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockName', models.TextField()),
                ('stackStatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_qty', models.IntegerField(default=0)),
                ('order_type', models.CharField(choices=[('Limit', 'Limit'), ('Market', 'Market')], max_length=20)),
                ('executed_qty', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('orderstatus', models.CharField(choices=[('PLACED', 'PLACED'), ('PROCESSED', 'PROCESSED'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], max_length=20)),
                ('orderdate', models.DateField(default=datetime.date.today)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.stock')),
            ],
        ),
    ]
