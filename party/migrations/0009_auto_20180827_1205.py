# Generated by Django 2.0.4 on 2018-08-27 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0008_order_orderdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='company',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='company',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]