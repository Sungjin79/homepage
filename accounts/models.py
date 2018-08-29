from django.db import models
from django.conf import settings

#from party import Company

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
#    company = models.ForeignKey(Company, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
