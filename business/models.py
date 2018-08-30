from django.db import models
from party.models import Company


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

    payterm_list = (
        ('prepaid', 'prepaid'),
        ('collect', 'collect')
    )

    payterm = models.CharField(max_length=7, choices=payterm_list)

    svcterm = models.CharField(max_length=9)

    incoterms = models.CharField(max_length=3)
    bltype = models.CharField(max_length=3)
    shipper = models.CharField(max_length=100)
    shipperlocation = models.CharField(max_length=5)
    shipperaddress = models.CharField(max_length=200)
    cnee = models.CharField(max_length=100)
    cneelocation = models.CharField(max_length=5)
    cneeaddress = models.CharField(max_length=200)
    noty = models.CharField(max_length=100)
    notylocation = models.CharField(max_length=5)
    notyaddress = models.CharField(max_length=200)
    noty2 = models.CharField(max_length=100)
    noty2location = models.CharField(max_length=5)
    noty2address = models.CharField(max_length=200)
    pickup = models.CharField(max_length=100)
    pickuplocation = models.CharField(max_length=5)
    pickupaddress = models.CharField(max_length=200)
    pickuptype = models.CharField(max_length=10)
    delivery = models.CharField(max_length=100)
    deliverylocation = models.CharField(max_length=5)
    deliveryaddress = models.CharField(max_length=200)
    deliverytype = models.CharField(max_length=10)
    initby = models.CharField(max_length=100)
    initdttm = models.CharField(max_length=14)
    upby = models.CharField(max_length=100)
    updttm = models.CharField(max_length=14)


class OrderDetail(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    itemqty = models.IntegerField()
    invoicevalue = models.IntegerField()
    invoicevaluecurr = models.CharField(max_length=3)
    itempkg = models.CharField(max_length=100) # max_length 안나와있음
    itempkgqty = models.IntegerField()
    vol = models.IntegerField()
    voluom = models.CharField(max_length=3)
    grosswgt = models.IntegerField()
    grosswgtuom = models.CharField(max_length=3)
    netwgt = models.IntegerField()
    netwgtuom = models.CharField(max_length=3)
    initby = models.CharField(max_length=100)
    initdttm = models.CharField(max_length=14)
    upby = models.CharField(max_length=100)
    updttm = models.CharField(max_length=14)
