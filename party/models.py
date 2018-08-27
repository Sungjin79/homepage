from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_type_list = (
        ('SHIPPER', 'Shipper Label'),
        ('LSP', 'LSP Label')
    )
    company_type = models.CharField(max_length=100, choices=company_type_list)
#    ci = models.ImageField(upload_to='%Y/%m/%d/front/', blank=True)

    def __str__(self):
        return self.company_name


class Item(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vol = models.IntegerField()
    vol_uom = models.CharField(max_length=3)
    grosswgt = models.IntegerField()
    grosswgt_uom = models.CharField(max_length=3)
    netwgt = models.IntegerField()
    netwgt_uom = models.CharField(max_length=3)
    commodity = models.CharField(max_length=15)
    hscode = models.CharField(max_length=15)
    level1 = models.CharField(max_length=100)
    level2 = models.CharField(max_length=100)
    level3 = models.CharField(max_length=100)
    level4 = models.CharField(max_length=100)


class ItemDetail(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_pkg = models.CharField(max_length=10)
    qty = models.IntegerField()
    doc_pkg = models.CharField(max_length=10)
    vol = models.IntegerField()
    vol_uom = models.CharField(max_length=3)
    grosswgt = models.IntegerField()
    grosswgt_uom = models.CharField(max_length=3)
    netwgt = models.IntegerField()
    netwgt_uom = models.CharField(max_length=3)


class Party(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    party = models.CharField(max_length=100)
    party_type_list = (
        ('CNEE', 'CNEE Label'),
        ('NOTY', 'NOTY Label'),
        ('PORT', 'PORT Label'),
    )
    party_type = models.CharField(max_length=10, choices=party_type_list)
    party_location = models.CharField(max_length=5)
    party_address = models.CharField(max_length=200)
    level1 = models.CharField(max_length=100)
    level2 = models.CharField(max_length=100)
    level3 = models.CharField(max_length=100)
    level4 = models.CharField(max_length=100)

    def __str__(self):
        return self.party


class Location(models.Model):
    location = models.CharField(max_length=5)
    language = models.CharField(max_length=5)
    location_type = models.CharField(max_length=10)
    location_detail = models.CharField(max_length=300)
    level1 = models.CharField(max_length=100)
    level2 = models.CharField(max_length=100)
    level3 = models.CharField(max_length=100)
    level4 = models.CharField(max_length=100)
    citycode = models.CharField(max_length=5)
    nation = models.CharField(max_length=2)


class LocationKeyword(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=10)


class Order(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



class OrderDetail(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

# 팝업 디자인 대신 페이지 전환으로
# 복합키 안쓰는 방식으로...
# ERD 필요.
