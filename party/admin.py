from django.contrib import admin

# Register your models here.
from party.models import Item, ItemDetail, Company, Party

admin.site.register(Item)
admin.site.register(ItemDetail)
admin.site.register(Company)
admin.site.register(Party)


