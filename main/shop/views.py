from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
import itertools
from django.db.models import Count
from .models import *

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def category(request):
  products = Product.objects.filter(status=True)
  try:
    shop_setup = ShopSettings.objects.get()
  except: 
    shop_setup = ShopSettings()
  count = int(request.GET.get('count', 16))
  page = request.GET.get("page", 1)

  paginator = Paginator(products, count)
  current_page = paginator.page(int(page))
  context = {
    "title": "Название товара",
    "products": current_page,
    "shop_setup": shop_setup,
    "count": count
  }

  return render(request, "pages/catalog/category.html", context)

def category_detail(request, slug):
  page = request.GET.get("page", 1)
  category = Category.objects.get(slug=slug)
  products = Product.objects.filter(category=category)
  count =  int(request.GET.get('count', 16))
  paginator = Paginator(products, count)
  current_page = paginator.page(int(page))

  context = {
    "category": category,
    "title": "Название товара",
    "products": current_page,
    "count": count
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

@csrf_exempt
def catalog_search(request):
    if request.method == "POST":
        try:
            data.json_loads(request.body)
            value = data.get("value")
            print(value)

            return JsonResponse({"value": value})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid JSON'}, status=400)
