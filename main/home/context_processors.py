from home.models import BaseSettings, SalesOffices
from shop.models import Category
from blog.models import BlogCategory
from service.models import Service
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}

def category_menu(request):
    return {'category_menu': Category.objects.all()}

def category_blog(request):
    return {'category_blog': BlogCategory.objects.all()}

def services(request):
    return {'services': Service.objects.filter(footer_view=True).order_by('-id')[:4]}

def offices(request):
    return {'offices': SalesOffices.objects.all()}

def static_theme_path(request):
    from django.conf import settings
    return {'STATIC_THEME_PATH': settings.STATIC_THEME_PATH}