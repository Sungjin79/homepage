"""Cargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from party.views import PartyCreateView, PartyListView, CompanyListView, CompanyCreateView, FindLocationKeyword, \
    PartyUpdateView, ItemListView, ItemCreateView, ItemUpdateView, ItemDetailListView, ItemDetailCreateView, \
    ItemDetailUpdateView
from business.views import OrderListView, OrderCreateView, OrderDetailListView, OrderDetailCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', PartyListView.as_view(), name='party-list'),
    path('party/create/', PartyCreateView.as_view(), name='party-create'),
    path('party/update/<int:pk>/', PartyUpdateView.as_view(), name='party-update'),

    path('item/', ItemListView.as_view(), name='item-list'),
    path('item/create/', ItemCreateView.as_view(), name='item-create'),
    path('item/update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),

    path('item/<int:item_id>/', ItemDetailListView.as_view(), name='item-detail-list'),
    path('item/<int:item_id>/create/', ItemDetailCreateView.as_view(), name='item-detail-create'),
    path('item/<int:item_id>/update/<int:pk>/', ItemDetailUpdateView.as_view(), name='item-detail-update'),

    path('company/', CompanyListView.as_view(), name='company-list'),
    path('company/create/', CompanyCreateView.as_view(), name='company-create'),
    path('location/keyword/<slug:keyword>/', FindLocationKeyword),

    path('business/order/', OrderListView.as_view(), name='order-list'),
    path('business/order/create/', OrderCreateView.as_view(), name='order-create'),

    path('business/order/<int:order_id>/', OrderDetailListView.as_view(), name='order-detail-list'),
    path('business/order/<int:order_id>/create/', OrderDetailCreateView.as_view(), name='order-detail-create'),
#    path('business/order/<int:order_id>/update/<int:pk>/', OrderDetailUpdateView.as_view(), name='order-detail-update'),
]
