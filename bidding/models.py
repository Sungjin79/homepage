from django.db import models
from django.conf import settings

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SectionCost(models.Model):
    executor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    cost = models.IntegerField()

    def __str__(self):
        return self.executor.username + ' ' + self.section.name


class CargoOwnerRecord(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    record = models.IntegerField()

    def __str__(self):
        return self.owner.username + ' ' + self.section.name


class Match(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    section_cost = models.ForeignKey(SectionCost, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.section.name + ' ' + self.owner.username + ' ' + self.section_cost.executor.username
