from django.urls import path, include
from . import views
app_name = 'news'
urlpatterns = [
    path('details/', views.News.as_view(), name='news'),
]
