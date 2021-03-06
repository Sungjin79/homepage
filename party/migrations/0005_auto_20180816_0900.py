# Generated by Django 2.0.4 on 2018-08-16 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0004_company_company_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=5)),
                ('language', models.CharField(max_length=5)),
                ('location_type', models.CharField(max_length=10)),
                ('location_detail', models.CharField(max_length=300)),
                ('level1', models.CharField(max_length=100)),
                ('level2', models.CharField(max_length=100)),
                ('level3', models.CharField(max_length=100)),
                ('level4', models.CharField(max_length=100)),
                ('citycode', models.CharField(max_length=5)),
                ('nation', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='LocationKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.Location')),
            ],
        ),
        migrations.AlterField(
            model_name='party',
            name='party_type',
            field=models.CharField(choices=[('CNEE', 'CNEE Label'), ('NOTY', 'NOTY Label'), ('PORT', 'PORT Label')], max_length=10),
        ),
    ]
