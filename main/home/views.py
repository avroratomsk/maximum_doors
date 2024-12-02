from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from home.models import BaseSettings, Gallery, GalleryCategory, HomeTemplate, RobotsTxt, Stock
from cart.models import Cart
from home.forms import CallbackForm, ContactForm, OrderSericeForm, ReviewsPopupForm
from home.callback_send import email_callback
from blog.models import Post
from shop.models import Category, Product
from reviews.models import Reviews
from django.http import JsonResponse
from django.db.models import Q

def callback(request):
  if request.method == "POST":
    form = CallbackForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      title = 'Заказ обратного звонка'
      messages = "Заказ обратного звонка:" + "\n" + "Имя: " +str(name) + "\n" + "Номер телефона: " + str(phone) + "\n"
      
      email_callback(messages, title)
      
      return JsonResponse({"success": "success"})
  else:
    return JsonResponse({'status': "error", 'errors': form.errors})
  
  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def contact_form(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      social = form.cleaned_data['social']
      title = 'Заказ обратного звонка'
      messages = "Заказ обратного звонка:" + "\n" + "Имя: " +str(name) + "\n" + "Номер телефона: " + str(phone) + "\n" + "\n" + "Способ связи: " + str(social) + "\n"
      
      email_callback(messages, title)
      
      return JsonResponse({"success": "success"})
    else:
      print(form)
  else:
    return JsonResponse({'status': "error", 'errors': form.errors})
  
  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def service_form(request):
  if request.method == "POST":
    form = OrderSericeForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      pagename = form.cleaned_data['service']
      title = 'Заказ обратного звонка'
      messages = "Заказ обратного звонка:" + "\n" + "Имя: " +str(name) + "\n" + "Номер телефон: " + str(phone) + "\n" + "Заказ услуги: " + str(pagename) + "\n"
      
      email_callback(messages, title)
      
      return JsonResponse({"success": "success"})
    else:
      print(form)
  else:
    return JsonResponse({'status': "error", 'errors': form.errors})
  
  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def consultation(request):
  if request.method == "POST":
    form = OrderSericeForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      pagename = form.cleaned_data['service']
      title = 'Консультация'
      messages = "Консультация:" + "\n" + "Имя: " +str(name) + "\n" + "Телефон: " + str(phone) + "\n" + "Проконсультировать по : " + str(pagename) + "\n"
      
      email_callback(messages, title)
      
      return JsonResponse({"success": "success"})
    else:
      print(form)
  else:
    return JsonResponse({'status': "error", 'errors': form.errors})
  
  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def index(request):
  try: 
    home_page = HomeTemplate.objects.get()
  except:
    home_page = HomeTemplate.objects.all()

  products = Product.objects.filter(status=True)[:4]
  posts = Post.objects.filter(status=True)
  context = {
    "home_page": home_page,
    "products": products,
    "posts": posts
  }
  return render(request, 'pages/index.html', context)


def gal_cat_detail(request, slug):
  category = GalleryCategory.objects.get(slug=slug)
  images = Gallery.objects.filter(category=category, cat_detail=True)
  context = {
    "category": category,
    "images": images,
  }
  
  return render(request, "pages/category-detail.html", context)

  
def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

def stock_product(request):
  page = request.GET.get("page", 1)
  products = Product.objects.filter(status=True, sale_price=True)
  
  paginator = Paginator(products, 16)
  current_page = paginator.page(int(page))
  context = {
    "products": products,
    "category_name": "Товары со скидкой",
  }
  
  return render(request, "pages/catalog/category-details.html", context)

def stock(request):
    stocks = Stock.objects.filter(status=True)
    news = Product.objects.filter(latest=True)
    populate = Product.objects.filter(quantity_purchase__gte=10)
    free_delivery = Product.objects.filter(free_shipping=True)
    
    context = {
        "stocks": stocks,
        "news": news,
        "populate": populate,
        "free_delivery": free_delivery,
    }
    
    return render(request, "pages/stock/stock.html", context)

def stock_detail(request, slug):
    stock = Stock.objects.get(slug=slug)
    
    context = {
        "stock": stock
    }
    
    return render(request, "pages/stock/stock_detail.html", context)
  
  
def gallery(request):
  gallery_category = GalleryCategory.objects.all().prefetch_related('categories')
  gallery = Gallery.objects.filter(is_active=True)
  
  context = {
    "gallery": gallery,
    "gallery_category": gallery_category,
  }
  
  return render(request, "pages/gallery.html", context)


def delivery(request):
  return render(request, "pages/delivery.html")

def robots_txt(request):
  try:
      robots_txt = RobotsTxt.objects.first()  # Получаем первую запись, т.к. нам нужен только один robots.txt
      content = robots_txt.content if robots_txt else "User-agent: *\nDisallow: /admin/"
  except RobotsTxt.DoesNotExist:
    content = "User-agent: *\nDisallow: /admin/"

  return HttpResponse(content, content_type="text/plain")