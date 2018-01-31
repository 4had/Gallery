from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.views.generic import View, ListView
from .models import Item, ItemImage

app_name = 'main'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    re_path('details/(?P<pk>\w+)/', views.Details.as_view(), name='details'),

    path('zoo/', views.ListView.as_view(queryset=ItemImage.objects.filter(category__category='zoo').order_by("-updated"), template_name='works/zoo_all.html'), name='zoo_all'),
    path('portraits/', views.ListView.as_view(queryset=ItemImage.objects.filter(category__category='portrait').order_by("-updated"), template_name='works/portraits_all.html'), name='portraits_all'),
    path('portraits_bw/', views.ListView.as_view(queryset=ItemImage.objects.filter(category__category='bw_portraits').order_by("-updated"), template_name='works/portraits_bw_all.html'), name='portraits_bw_all'),
    path('landscapes/', views.ListView.as_view(queryset=ItemImage.objects.filter(category__category='landscape').order_by("-updated"), template_name='works/landscapes_all.html'), name='landscapes_all'),
    path('flowers/', views.ListView.as_view(queryset=ItemImage.objects.filter(category__category='flower').order_by("-updated"), template_name='works/flowers_all.html'), name='flowers_all'),


    path('about/', views.AboutView.as_view(), name='about'),
    path('lessons/', views.LessonsView.as_view(), name='lessons'),


    path('add/', views.ItemAdd.as_view(), name='item_add'),
    re_path('comment/(?P<pk>\w+)/delete/$', views.CommentDelete.as_view(), name='comment_delete')


]
