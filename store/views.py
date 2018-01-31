from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from item.models import *
# Create your views here.


class StoreView(View):

    def get(self, request):
        zoo = ItemImage.objects.filter(category__category='zoo')
        portrait = ItemImage.objects.filter(category__category='portrait')
        bw_portraits = ItemImage.objects.filter(category__category='bw_portraits')
        landscape = ItemImage.objects.filter(category__category='landscape')
        flowers = ItemImage.objects.filter(category__category='flower')
        all = ItemImage.objects.filter(is_active=True)
        return render(request, 'store/store_index.html', locals())
