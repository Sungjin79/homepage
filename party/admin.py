from django.contrib import admin

# Register your models here.
from party.models import Item, ItemDetail, Company, Party, Location, LocationKeyword

admin.site.register(Item)
admin.site.register(ItemDetail)
admin.site.register(Company)
admin.site.register(Party)
admin.site.register(Location)
admin.site.register(LocationKeyword)
