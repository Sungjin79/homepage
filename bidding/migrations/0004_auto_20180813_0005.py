# Generated by Django 2.1 on 2018-08-12 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_auto_20180619_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioncost',
            name='executor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
