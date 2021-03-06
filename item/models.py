from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=120, default=None)

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Item(models.Model):

    name = models.CharField('Name', max_length=256)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    price = models.FloatField('Price')
    category = models.ForeignKey(Category, default=0, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ['created']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def get_absolute_url(self):
        return reverse('main:works')


class ItemImage(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='')
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, default=0, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.item

    class Meta:
        verbose_name = 'Item\'s image'
        verbose_name_plural = 'Images'


class Comment(models.Model):
    post = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(max_length=500)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    class Meta:
        ordering = ['created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'




















