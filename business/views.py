from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView
from business.models import Order
from django.urls import reverse

from party.models import Company


class OrderListView(ListView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    fields = ('biztype', 'rdd',  'status',
    'payterm',
    'svcterm',
    'incoterms',
    'bltype',
    'shipper',
    'shipperlocation',
    'shipperaddress',
    'cnee',
    'cneelocation',
    'cneeaddress',
    'noty',
    'notylocation',
    'notyaddress',
    'noty2',
    'noty2location',
    'noty2address',
    'pickup',
    'pickuplocation',
    'pickupaddress',
    'pickuptype',
    'delivery',
    'deliverylocation',
    'deliveryaddress',
    'deliverytype',
    'initby',
    'initdttm',
    'upby',
    'updttm')

    def get_success_url(self):
        return reverse('order-list')

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['company_list'] = Company.objects.raw('select * from party_company')
        #Company.objects.all()

        print(Company.objects.all().query)



        return context
