from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CommentForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class Index(View):

    def get(self, request):
        zooimg = ItemImage.objects.filter(category__category='zoo')
        portrait = ItemImage.objects.filter(category__category='portrait')
        bw_portraits = ItemImage.objects.filter(category__category='bw_portraits')
        landscape = ItemImage.objects.filter(category__category='landscape')
        flowers = ItemImage.objects.filter(category__category='flower')
        front = [flowers.reverse()[0], portrait.reverse()[0]]

        return render(request, 'main/index.html', locals())



class LessonsView(View):

    def get(self, request):
        return render(request, 'main/lessons.html', locals())


class AboutView(View):

    def get(self, request):
        return render(request, 'main/about.html', locals())




# class Zoo(View):
#
#     def get(self, request):
#         worksImg = ItemImage.objects.all()
#         return render(request, 'main/works.html', locals())


class ItemAdd(CreateView):
    template_name = 'forms/item_add_form.html'
    model = Item
    fields = '__all__'


class Details(DetailView):

    def get(self, request, pk):
        post = get_object_or_404(Item, pk=pk)
        comment = Comment.objects.filter(post=post)
        comment_form = CommentForm()
        return render(request, 'main/picture_page.html', locals())

    def post(self, request, pk):
        post = Item.objects.get(pk=pk)
        comment = Comment.objects.filter(post=post)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid:
            comment_post = comment_form.save(commit=False)
            comment_post.user = request.user
            comment_post.post = post
            comment_post.save()

            return render(request, 'main/picture_page.html', locals())


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('main:works')




