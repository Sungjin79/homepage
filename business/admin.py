from django.contrib import admin

from business.models import Order, OrderDetail

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
