# Generated by Django 2.0.4 on 2018-08-30 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0009_auto_20180827_1205'),
        ('business', '0002_auto_20180829_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('itemqty', models.IntegerField()),
                ('invoicevalue', models.IntegerField()),
                ('invoicevaluecurr', models.CharField(max_length=3)),
                ('itempkg', models.CharField(max_length=100)),
                ('itempkgqty', models.IntegerField()),
                ('vol', models.IntegerField()),
                ('voluom', models.CharField(max_length=3)),
                ('grosswgt', models.IntegerField()),
                ('grosswgtuom', models.CharField(max_length=3)),
                ('netwgt', models.IntegerField()),
                ('netwgtuom', models.CharField(max_length=3)),
                ('initby', models.CharField(max_length=100)),
                ('initdttm', models.CharField(max_length=14)),
                ('upby', models.CharField(max_length=100)),
                ('updttm', models.CharField(max_length=14)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.Company')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Order')),
            ],
        ),
    ]