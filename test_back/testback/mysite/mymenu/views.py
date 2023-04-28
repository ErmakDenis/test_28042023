from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return render(request,'mymenu/index.html')

from django.shortcuts import render, get_object_or_404
from .models import Category


# Было если честно лениво делать еще определение текущей станицы, в любом случае это делалось бы через слаг b
def category_view(request):#, slug

    category = get_object_or_404(Category,slug='mymenu')#, slug=slug
    sub_categories = category.children.all().order_by('name')
    return render(request, 'mymenu/category.html',
                  {'category': category, 'sub_categories': sub_categories})




