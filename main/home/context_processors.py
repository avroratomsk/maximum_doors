from home.models import BaseSettings
from shop.models import Category
from blog.models import BlogCategory
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}

def category_menu(request):
    return {'category_menu': Category.objects.all()}

def category_blog(request):
    return {'category_blog': BlogCategory.objects.all()}

def static_theme_path(request):
    from django.conf import settings
    return {'STATIC_THEME_PATH': settings.STATIC_THEME_PATH}