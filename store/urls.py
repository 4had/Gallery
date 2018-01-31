from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.views.generic import View, ListView
from item.models import Item, ItemImage

app_name = 'store'

urlpatterns = [
    path('', views.StoreView.as_view(), name='store_index'),
]
