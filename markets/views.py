from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class MarketListView(ListView):
    model = Market
    template_name = "markets/markets_list.html"


class MarketProductsListView(ListView):
    model = MarketList
    template_name = 'markets/market.html'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(name__startswith=self.kwargs['user'])

