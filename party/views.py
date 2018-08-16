from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView

from party.models import Party, Company, LocationKeyword
from django.http import JsonResponse, HttpResponse
from django.urls import reverse


class PartyListView(ListView):
    model = Party


class PartyCreateView(CreateView):
    model = Party
    fields = ('company', 'party', 'party_type', 'party_location', 'party_address', 'level1', 'level2', 'level3', 'level4')

    def get_success_url(self):
        return reverse('party-list')


class CompanyListView(ListView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = ('company_name', 'company_type')


def FindLocationKeyword(request, keyword):
    result = LocationKeyword.objects.filter(keyword__contains=keyword)
#    return HttpResponse(str(keyword))
    #return JsonResponse(result)
    if len(result) > 0:
        return HttpResponse(result[0].location.location)
    else:
        return HttpResponse('')
