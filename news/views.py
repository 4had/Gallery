from django.shortcuts import render
from django.views.generic import DetailView, View, DeleteView, UpdateView, CreateView
# Create your views here.
from .models import NewOnSite


class News(View):

    def get(self, request):
        New = NewOnSite.objects.all()
        return render(request, 'News/News.html', locals())