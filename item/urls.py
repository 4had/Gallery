from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.views import View
from .models import Item

app_name = 'main'

urlpatterns = [
    re_path('details/(?P<pk>\w+)/', views.Details.as_view(), name='details'),
    path('', views.Index.as_view(), name='index'),

    path('add/', views.ItemAdd.as_view(), name='item_add'),
    re_path('comment/(?P<pk>\w+)/delete/$', views.CommentDelete.as_view(), name='comment_delete')


]
