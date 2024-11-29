from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
import itertools
from .services import *
from django.db.models import Count
from .models import *

def category(request):
  products = Product.objects.filter(status=True)
  try:
    shop_setup = ShopSettings.objects.get()
  except: 
    shop_setup = ShopSettings()
  page = request.GET.get("page", 1)
  
          
  paginator = Paginator(products, 16)
  current_page = paginator.page(int(page))
  context = {
    "title": "Название товара",
    "products": current_page,
    "shop_setup": shop_setup
  }
  
  return render(request, "pages/catalog/category.html", context)


def category_detail(request, slug):
  page = request.GET.get("page", 1)
  category = Category.objects.get(slug=slug)
  # chars = CharName.objects.filter(group=None)
  products = Product.objects.filter(category=category).order_by('model')
    
  paginator = Paginator(products, 16)
  current_page = paginator.page(int(page))
  
  context = {
    "category": category,
    "title": "Название товара",
    "products": current_page,
  }
  
  return render(request, "pages/catalog/category-details.html", context)

def product(request, slug):
  product = Product.objects.get(slug=slug)
  properties = Properties.objects.filter(parent=product)
  products = Product.objects.filter(status=True).exclude(id=product.id)[:4]
   
  context = {
    "product": product,
    "products": products,
    "properties": properties,
  }
  return render(request, "pages/catalog/product.html", context)
