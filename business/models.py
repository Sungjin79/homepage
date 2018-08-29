from django.db import models

# Create your models here.
class Order(models.Model):
    biztype_list = (
        ('EXPORT', 'Export biztype'),
        ('IMPORT', 'Import biztype')
    )

    biztype = models.CharField(max_length=10, choices=biztype_list)
    rdd = models.CharField(max_length=14)

    status_list = (
        ('OPEN', 'Open Status'),
        ('PROCEEDING', 'Proceeding'),
        ('COMPLETE', 'Complete')
    )

    status = models.CharField(max_length=10, choices=status_list)
