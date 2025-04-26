import math
import os
import zipfile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from admin.forms import BlogSettingsForm, CategoryForm, ColorProductForm, GalleryCategoryForm, GalleryCategorySettingsForm, GalleryForm, GlobalSettingsForm, HomeTemplateForm, PostForm, BlogCategoryForm, ProductForm, ProductImageForm, RobotsForm, ServiceForm, ServicePageForm, ShopSettingsForm, StockForm, SubdomainForm, UploadFileForm
from home.models import BaseSettings, Gallery, GalleryCategory, HomeTemplate, RobotsTxt, Stock
from blog.models import BlogSettings, Post, BlogCategory
from main.settings import BASE_DIR
from subdomain.models import Subdomain
from service.models import Service, ServicePage

from shop.models import ColorProduct, Product, Category, ProductImage, Properties, ShopSettings
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
import openpyxl
import pandas as pd
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import user_passes_test
import uuid
import numpy as np
import math

path = f"{BASE_DIR}/upload/upload.zip"
path_to_excel = f"{BASE_DIR}/upload/upload.xlsx"
folder = 'upload/'

def unzip_archive():
  with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall()


def get_unique_slug(model, base_slug):
    slug = base_slug
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug

def import_products_from_excel(file_path):
    Product.objects.all().delete()
    Properties.objects.all().delete()
    Category.objects.all().delete()

    # Загружаем данные из Excel
    df = pd.read_excel(file_path, engine='openpyxl')

    for _, row in df.iterrows():
      article=row[0]
      name = row[1].strip()
      slug = get_unique_slug(Product, slugify(name))
      category = row[2]
      category_slug = slugify(category)

      try:
        category = Category.objects.get(slug=category_slug)
      except ObjectDoesNotExist:
        if not Category.objects.filter(name=category).exists():
          category = Category.objects.create(
            name=category,
            slug=category_slug
        )
      try:
        manufacturer = row[3]
      except:
        pass

      manufacturer_description = row[4]

      try:
        colors = row[5]
        if isinstance(colors, float) and math.isnan(colors):  # Проверяем, является ли значением NaN
          colors = ""
      except:
        colors = ""

      image = f"goods/{row[6]}"


      try:
          price = row[7]
          if isinstance(price, float) and math.isnan(price):  # Проверяем, является ли значением NaN
            price = 0
      except:
          price = 0

      try:
        installment = row[8]
        if isinstance(installment, float) and math.isnan(installment):  # Проверяем, является ли значением NaN
          installment = ""
      except:
        installment = ""

      try:
          properties = row[10]
      except:
          properties = ""

      sale = 0

      try:
          new_product = Product.objects.create(
              article=article,
              name=name,
              slug=slug,
              category=category,
              manufacturer=manufacturer,
              manufacturer_description=manufacturer_description,
              colors=colors,
              image=image,
              price=price,
              installment=installment,
              sale=sale,
          )
      except IntegrityError:
          print(f"Duplicate slug detected: {slug}, generating a new one.")
          slug = get_unique_slug(Product, slug)
          new_product = Product.objects.create(
              article=article,
              name=name,
              slug=slug,
              category=category,
              manufacturer=manufacturer,
              manufacturer_description=manufacturer_description,
              colors=colors,
              image=image,
              price=price,
              installment=installment,
              sale=sale,
          )

      try:
          properties = properties.split(';')
          for ch in properties:
            try:
              new_properties = Properties.objects.create(
                parent = new_product,
                name = ch.split(":")[0].strip(),
                value = ch.split(":")[1].strip()
              )
            except Exception as e:
                pass
      except:
          pass

# @user_passes_test(lambda u: u.is_superuser)
# def sidebar_show(request): 
   
#     request.session['sidebar'] = 'True'
    
#     return redirect('admin')

# @user_passes_test(lambda u: u.is_superuser)
import urllib.parse

@user_passes_test(lambda u: u.is_superuser)
def admin(request):
  #import_products_from_excel(path_to_excel)

  # unzip_archive()
  """Данная предстовление отобразает главную страницу админ панели"""
  return render(request, "page/index.html")

def admin_settings(request):
  try:
    settings = BaseSettings.objects.get()
  except:
    settings = BaseSettings()
    settings.save()
  
  if request.method == "POST":
    form_new = GlobalSettingsForm(request.POST, request.FILES, instance=settings)
    if form_new.is_valid():
      form_new.save()
      
      # subprocess.call(["touch", RESET_FILE])
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "settings/general_settings.html", {"form": form_new})

  settings = BaseSettings.objects.get()

  form = GlobalSettingsForm(instance=settings)
  context = {
    "form": form,
    "settings":settings
  }  

  return render(request, "settings/general_settings.html", context)

def robots(request):
  try:
    robots = RobotsTxt.objects.get()
  except:
    robots = RobotsTxt()
    robots.save()
  
  if request.method == "POST":
    form_new = RobotsForm(request.POST, request.FILES, instance=robots)
    if form_new.is_valid():
      form_new.save()
      
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "settings/robots.html", {"form": form_new})

  robots = RobotsTxt.objects.get()

  form = RobotsForm(instance=robots)
  
  context = {
    "form": form,
    "robots":robots
  }  

  return render(request, "settings/robots.html", context)

def admin_product(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию
  """
  page = request.GET.get('page', 1)
  products = Product.objects.all()
  paginator = Paginator(products, 20)
  current_page = paginator.page(int(page))

  context = {
    "items": current_page
  }
  return render(request, "shop/product/product.html", context)

def product_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  product = Product.objects.get(id=pk)
  product_image = ProductImage.objects.filter(parent=product)
  form = ProductForm(instance=product)

  form_new = ProductForm(request.POST, request.FILES, instance=product)
  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      product = Product.objects.get(slug=request.POST['slug'])
      images = request.FILES.getlist('src')

      for image in images:
          img = ProductImage(parent=product, src=image)
          img.save()

      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, 'shop/product/product_edit.html', {'form': form_new})
  context = {
    "form":form,
    "product_image": product_image,
  }
  return render(request, "shop/product/product_edit.html", context)

def product_add(request):
  form = ProductForm()

  if request.method == "POST":
    form_new = ProductForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_product')
    else:
      return render(request, "shop/product/product_add.html", {"form": form_new})

  context = {
    "form": form
  }

  return render(request, 'shop/product/product_add.html', context)

def product_delete(request,pk):
  product = Product.objects.get(id=pk)
  product.delete()

  return redirect('admin_product')

def admin_home_page(request):
  try:
    settings = HomeTemplate.objects.get()
  except:
    settings = HomeTemplate()
    settings.save()
  
  if request.method == "POST":
    form_new = HomeTemplateForm(request.POST, request.FILES, instance=settings)
    if form_new.is_valid():
      form_new.save()
      
      # subprocess.call(["touch", RESET_FILE])
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "home-page/home-page.html", {"form": form_new})

  settings = HomeTemplate.objects.get()

  form = HomeTemplateForm(instance=settings)
  context = {
    "form": form,
    "settings":settings
  }  

  return render(request, "home-page/home-page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_shop(request):
  try:
    shop_setup = ShopSettings.objects.get()
    form = ShopSettingsForm(instance=shop_setup)
  except:
    form = ShopSettingsForm()
    
  if request.method == "POST":
    try:
      shop_setup = ShopSettings.objects.get()
    except ShopSettings.DoesNotExist:
      shop_setup = None
    form_new = ShopSettingsForm(request.POST, request.FILES, instance=shop_setup)
    
    if form_new.is_valid:
      form_new.save()
      
      return redirect('admin_shop')
    else:
      return render(request, "shop/settings.html", {"form": form})
  
  context = {
    "form": form,
  }  
  return render(request, "shop/settings.html", context)

def blog_settings(request):
  try:
    setup = BlogSettings.objects.get()
    form = BlogSettingsForm(instance=setup)
  except:
    form = BlogSettingsForm()
    
  if request.method == "POST":
    try:
      setup = BlogSettings.objects.get()
    except BlogSettings.DoesNotExist:
      setup = None
    form_new = BlogSettingsForm(request.POST, request.FILES, instance=setup)
    
    if form_new.is_valid:
      form_new.save()
      
      return redirect('.')
    else:
      return render(request, "blog/blog_post/blog_post.html", {"form": form})
  
  context = {
    "form": form,
  }  
  return render(request, "blog/blog_post/blog_post.html", context)

def gallery_settings(request):
  try:
    setup = GalleryCategory.objects.get()
    form = GalleryCategorySettingsForm(instance=setup)
  except:
    form = GalleryCategorySettingsForm()
    
  if request.method == "POST":
    try:
      setup = BlogSettings.objects.get()
    except BlogSettings.DoesNotExist:
      setup = None
    form_new = GalleryCategorySettingsForm(request.POST, request.FILES, instance=setup)
    
    if form_new.is_valid:
      form_new.save()
      
      return redirect('.')
    else:
      return render(request, "gallery/gallery_settings.html", {"form": form})
  
  context = {
    "form": form,
  }  
  return render(request, "gallery/gallery_settings.html", context)


def admin_attribute(request):
  chars = ProductSpecification.objects.all()
  
  context = {
    "title": "Характеристики товара",
    "chars": chars,
  }
  
  return render(request, "shop/char/char.html", context)

folder = 'upload/'

from PIL import Image

def upload_goods(request):
    form = UploadFileForm()
    if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)
      if form.is_valid():
          file = request.FILES['file']
          
          destination = open(os.path.join('upload/', file.name), 'wb+')
          for chunk in file.chunks():
              destination.write(chunk)
          destination.close()
              
          # Распаковка архива
          with zipfile.ZipFile('upload/upload.zip', 'r') as zip_ref:
              zip_ref.extractall('media/')
              
          # Удаление загруженного архива
          os.remove('upload/upload.zip')
          
          # Сжатие фотографий
          for filename in os.listdir('media/upload'):
            
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.JPG') or filename.endswith('.JPEG') or filename.endswith('.jpeg'):
              with Image.open(os.path.join('media/upload', filename)) as img:
                temp = filename.replace('.jpeg', '')
                temp_one = temp.replace('№', '')
                temp_b = temp_one.replace('В', 'B')
                temp_e = temp_one.replace('Э', 'E')
                img.save(os.path.join('media/goods', temp_e), quality=60)  # quality=60 для JPEG файла
                
          # Очистка временной папки
          os.system('rm -rf media/upload')
          return redirect('upload-succes')
      else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})

def upload_succes(request):
  return render(request, "upload/upload-succes.html")

from pytils.translit import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

def admin_category(request):
  categorys = Category.objects.all()
  
  context ={
    "items": categorys,
  }
  return render(request, "shop/category/category.html", context)

def category_add(request):
  form = CategoryForm()
  if request.method == "POST":
    form_new = CategoryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_category")
    else:
      return render(request, "shop/category/category_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  return render(request, "shop/category/category_add.html", context)

def category_edit(request, pk):
  categorys = Category.objects.get(id=pk)
  form = CategoryForm(request.POST, request.FILES, instance=categorys)
  
  if request.method == "POST":
    
    if form.is_valid():
      form.save()
      return redirect("admin_category")
    else:
      return render(request, "shop/category/category_edit.html", {"form": form, 'image_path': image_path})
  
  context = {
    "form": CategoryForm(instance=categorys),
    "categorys": categorys
  }

  return render(request, "shop/category/category_edit.html", context)

def category_delete(request, pk):
  category = Category.objects.get(id=pk)
  category.delete()
  
  return redirect('admin_category')

def admin_home(request):
  try:
    home_page = HomeTemplate.objects.get()
  except:
    home_page = HomeTemplate()
    home_page.save()
    
  if request.method == "POST":
    form_new = HomeTemplateForm(request.POST, request.FILES, instance=home_page)
    if form_new.is_valid():
      form_new.save()
      
      # subprocess.call(["touch", RESET_FILE])
      return redirect("admin")
    else:
      return render(request, "static/home_page.html", {"form": form_new})
  
  home_page = HomeTemplate.objects.get()
  
  form = HomeTemplateForm(instance=home_page)
  context = {
    "form": form,
    "home_page":home_page
  }  
  
  return render(request, "static/home_page.html", context)

def admin_service_page(request):
  try:
    service_page = ServicePage.objects.get()
  except:
    service_page = ServicePage()
    service_page.save()
    
  if request.method == "POST":
    form_new = ServicePage(request.POST, request.FILES, instance=service_page)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin")
    else:
      return render(request, "serv/serv_settings.html", {"form": form_new})
  
  service_page = HomeTemplate.objects.get()
  
  form = HomeTemplateForm(instance=service_page)
  context = {
    "form": form,
    "service_page":service_page
  }  
  
  return render(request, "static/home_page.html", context)

def admin_stock(request):
  stocks = Stock.objects.all()

  context = {
    "stocks": stocks
  }

  return render(request, "stock/stock.html", context)

def stock_add(request):
  form = StockForm()
  
  if request.method == "POST":
    form_new = StockForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_stock")
    else: 
      return render(request, "stock/stock_add.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "stock/stock_add.html", context)

def stock_edit(request, pk):
  stock = Stock.objects.get(id=pk)
  form = StockForm(instance=stock)
  if request.method == "POST":
    form_new = StockForm(request.POST, request.FILES, instance=stock)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_stock")
    else:
      return render(request, "stock/stock_edit.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "stock/stock_edit.html", context)

def stock_delete(request, pk):
  stock = Stock.objects.get(id=pk)
  stock.delete()
  return redirect("admin_stock")

def admin_service(request):
  services = Service.objects.all()
  
  context = {
    "services": services
  }
  
  return render(request, "serv/admin_serv.html", context)

def service_add(request):
  form = ServiceForm()
  
  if request.method == "POST":
    form_new = ServiceForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_service")
    else: 
      return render(request, "serv/serv_add.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_add.html", context)

def service_edit(request, pk):
  services = Service.objects.get(id=pk)
  form = ServiceForm(instance=services)
  if request.method == "POST":
    form_new = ServiceForm(request.POST, request.FILES, instance=services)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_service")
    else:
      return render(request, "serv/stock_edit.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_edit.html", context)

def service_delete(request, pk):
  service = Service.objects.get(id=pk)
  service.delete()
  return redirect("admin_service")

def admin_color(request):
  items = ColorProduct.objects.all()
  
  context = {
    "items": items,  
  }
  
  return render(request, "shop/color/color.html", context)


def admin_color_add(request):
  form = ColorProductForm()
  
  if request.method == "POST":
    form_new = ColorProductForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_color')
    else:
      return render(request, "shop/color/color_add.html", { "form": form_new })
    
  context = {
    "form": form, 
  }  
    
  return render(request, "shop/color/color_add.html", context)

def admin_color_edit(request, pk):
  item = ColorProduct.objects.get(id=pk)
  
  if request.method == "POST":
    form_new = ColorProductForm(request.POST, request.FILES, instance=item)
    
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_color')
    else:
      return render(request, "shop/color/color_edit.html", { "form": form_new })
  
  form = ColorProductForm(instance=item)
  context = {
    "form": form,
  }  
    
  return render(request, "shop/color/color_edit.html", context)

def admin_color_delete(request, pk):
  subdomain = Subdomain.objects.get(id=pk)
  subdomain.delete()
  return redirect(request.META.get('HTTP_REFERER'))

def admin_gallery(request):
  items = Gallery.objects.all()
  
  context = {
    "items": items,  
  }
  
  return render(request, "gallery/gallery.html", context)


def admin_gallery_add(request):
  form = GalleryForm()
  
  if request.method == "POST":
    form_new = GalleryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_gallery')
    else:
      return render(request, "gallery/gallery_add.html", { "form": form_new })
    
  context = {
    "form": form, 
  }  
    
  return render(request, "gallery/gallery_add.html", context)

def admin_gallery_edit(request, pk):
  item = Gallery.objects.get(id=pk)
  
  if request.method == "POST":
    form_new = GalleryForm(request.POST, request.FILES, instance=item)
    
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_gallery')
    else:
      return render(request, "gallery/gallery_edit.html", { "form": form_new })
  
  form = GalleryForm(instance=item)
  context = {
    "form": form,
  }  
    
  return render(request, "gallery/gallery_edit.html", context)

def admin_color_delete(request, pk):
  subdomain = Subdomain.objects.get(id=pk)
  subdomain.delete()
  return redirect(request.META.get('HTTP_REFERER'))


def admin_gallery_category(request):
  items = GalleryCategory.objects.all()
  
  context = {
    "items": items,
  }
  
  return render(request, "gallery/gallery_category.html", context)


def gallery_category_add(request):
  form = GalleryCategoryForm()
  
  if request.method == "POST":
    form_new = GalleryCategoryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_gallery_category')
    else:
      return render(request, "gallery/gallery_category_add.html", { "form": form_new })
    
  context = {
    "form": form, 
  }  
    
  return render(request, "gallery/gallery_category_add.html", context)

def gallery_category_edit(request, pk):
  item = GalleryCategory.objects.get(id=pk)
  
  if request.method == "POST":
    form_new = GalleryCategoryForm(request.POST, request.FILES, instance=item)
    
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_gallery')
    else:
      return render(request, "gallery/gallery_category_edit.html", { "form": form_new })
  
  form = GalleryCategoryForm(instance=item)
  context = {
    "form": form,
  }  
    
  return render(request, "gallery/gallery_category_edit.html", context)

def gallery_category_delete(request):
  pass



def article(request):
  items = Post.objects.all()
  
  context ={
    "items": items,
  }
  return render(request, "blog/blog_post/blog_post.html", context)

def article_add(request):
  form = PostForm()
  if request.method == "POST":
    form_new = PostForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("article")
    else:
      return render(request, "blog/blog_post/post_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, "blog/blog_post/post_add.html", context)

def article_edit(request, pk):
  item = Post.objects.get(id=pk)
  form = PostForm(request.POST, request.FILES, instance=item)
  
  if request.method == "POST":
    
    if form.is_valid():
      form.save()
      return redirect("article")
    else:
      return render(request, "blog/blog_post/post_edit.html", {"form": form, 'image_path': image_path})
  
  context = {
    "form": PostForm(instance=item),
    "item": item
  }

  return render(request, "blog/blog_post/post_edit.html", context)

def article_delete(request, pk):
  category = Post.objects.get(id=pk)
  category.delete()
  
  return redirect(request.META.get("HTTP_REFERER"))

def category_blog_settings(request):
    return render(request, "blog/blog_category/blog_category.html", context)

def category_blog(request):
  items = BlogCategory.objects.all()

  context ={
    "items": items,
  }
  return render(request, "blog/blog_category/blog_category.html", context)

def category_blog_add(request):
  form = BlogCategoryForm()
  if request.method == "POST":
    form_new = BlogCategoryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("category_blog")
    else:
      return render(request, "blog/blog_category/blog_category_add.html", {"form": form_new})

  context = {
    "form": form
  }

  return render(request, "blog/blog_category/blog_category_add.html", context)

def category_blog_edit(request, pk):
  item = BlogCategory.objects.get(id=pk)
  form = BlogCategoryForm(request.POST, request.FILES, instance=item)

  if request.method == "POST":

    if form.is_valid():
      form.save()
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "blog/blog_category/blog_category_edit.html", {"form": form, 'image_path': image_path})

  context = {
    "form": BlogCategoryForm(instance=item),
    "item": item
  }

  return render(request, "blog/blog_category/blog_category_edit.html", context)

def category_blog_remove(request, pk):
  category = BlogCategory.objects.get(id=pk)
  category.delete()

  return redirect(request.META.get('HTTP_REFERER'))
