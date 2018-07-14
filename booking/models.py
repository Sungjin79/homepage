from django.db import models
from django.conf import settings

# Create your models here.
class Booking(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    goods = models.IntegerField()


