from home.models import BaseSettings
from shop.models import Category 
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}

def category_menu(request):
    return {'category_menu': Category.objects.filter(add_menu=True)}

def static_theme_path(request):
    from django.conf import settings
    return {'STATIC_THEME_PATH': settings.STATIC_THEME_PATH}