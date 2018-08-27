from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView

from party.models import Party, Company, LocationKeyword, Item, ItemDetail
from django.http import JsonResponse, HttpResponse
from django.urls import reverse


class ItemListView(ListView):
    model = Item


class ItemCreateView(CreateView):
    model = Item

    fields = ('company','vol','vol_uom', 'grosswgt','grosswgt_uom','netwgt','netwgt_uom','commodity','hscode', 'level1', 'level2', 'level3', 'level4')

    def get_success_url(self):
        return reverse('item-list')


class ItemUpdateView(UpdateView):
    model = Item

    fields = ('company','vol','vol_uom', 'grosswgt','grosswgt_uom','netwgt','netwgt_uom','commodity','hscode', 'level1', 'level2', 'level3', 'level4')

    def get_success_url(self):
        return reverse('item-list')


class ItemDetailListView(ListView):
    model = ItemDetail

    def get_queryset(self):
        return ItemDetail.objects.filter(item=self.kwargs['item_id'])

    def get_context_data(self, **kwargs):
        context = super(ItemDetailListView, self).get_context_data(**kwargs)
        context['item_id'] = self.kwargs['item_id']

        return context


class ItemDetailCreateView(CreateView):
    model = ItemDetail

    fields = ('company','item','item_pkg','qty', 'doc_pkg','vol','vol_uom','grosswgt','grosswgt_uom','netwgt','netwgt_uom',)

    def get_success_url(self):
        return reverse('item-list')


class ItemDetailUpdateView(UpdateView):
    model = ItemDetail

    fields = ('company','item_pkg','qty', 'doc_pkg','vol','vol_uom','grosswgt','grosswgt_uom','netwgt','netwgt_uom',)

    def get_success_url(self):
        return reverse('item-list')


class PartyListView(ListView):
    model = Party


class PartyCreateView(CreateView):
    model = Party
    fields = ('company', 'party', 'party_type', 'party_location', 'party_address', 'level1', 'level2', 'level3', 'level4')

    def get_success_url(self):
        return reverse('party-list')


class PartyUpdateView(UpdateView):
    model = Party
    fields = ('company', 'party', 'party_type', 'party_location', 'party_address', 'level1', 'level2', 'level3', 'level4')

    def get_success_url(self):
        return reverse('party-list')


class CompanyListView(ListView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = ('company_name', 'company_type')

    def get_success_url(self):
        return reverse('company-list')


def FindLocationKeyword(request, keyword):
    result = LocationKeyword.objects.filter(keyword__contains=keyword)
#    return HttpResponse(str(keyword))
    #return JsonResponse(result)
    if len(result) > 0:
        return HttpResponse(result[0].location.location)
    else:
        return HttpResponse('')
