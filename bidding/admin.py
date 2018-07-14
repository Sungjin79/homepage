from django.contrib import admin

# Register your models here.
from bidding.models import Section, SectionCost, Match, CargoOwnerRecord

admin.site.register(Section)
admin.site.register(SectionCost)
admin.site.register(CargoOwnerRecord)
admin.site.register(Match)