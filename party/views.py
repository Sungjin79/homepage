from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView

from party.models import Party, Company


class PartyListView(ListView):
    model = Party


class PartyCreateView(CreateView):
    model = Party
    fields = ('company', 'party', 'party_type', 'party_location', 'party_address', 'level1', 'level2', 'level3', 'level4')


class CompanyListView(ListView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = ('company_name', 'company_type')