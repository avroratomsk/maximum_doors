from django import forms
from home.models import BaseSettings, Works, Production, Gallery, GalleryCategory, HomeTemplate, RobotsTxt, Stock, About, Delivery,SalesOffices, ContactTemplate
from blog.models import BlogSettings, Post, BlogCategory
from subdomain.models import Subdomain, SubdomainContact
from service.models import Service, ServicePage
from shop.models import Category, ColorProduct, Product, ProductImage, ShopSettings,Properties
from .widgets import CustomImageWidget
from django_ckeditor_5.widgets import CKEditor5Widget

INPUT_CLASS = "form__controls"

class UploadFileForm(forms.Form):
    file = forms.FileField()

class GlobalSettingsForm(forms.ModelForm):
  """ Form, глобальные и общие настройки сайта(лого, телефон, email)"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  class Meta:
    model = BaseSettings
    fields = "__all__"
    
    widgets = {
        'phone_one': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'phone': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'time_work': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'email': forms.EmailInput(attrs={
            'class': INPUT_CLASS
        }),
        'address': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_title': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_description': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'description':CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        )
    }
    
class RobotsForm(forms.ModelForm):
  
  class Meta:
    model = RobotsTxt
    fields = "__all__"
    
    widgets = {'content': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 30 }),}

class ShopSettingsForm(forms.ModelForm):
  """ Form, отвечает за создание товара и редактирование товара"""
  
  class Meta:
      model = ShopSettings
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_title': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_description': forms.Textarea(attrs={
              'class': 'form__controls',
              "id": "meta_description"
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
      }
      
class BlogSettingsForm(forms.ModelForm):
  class Meta:
      model = BlogSettings
      fields = "__all__"
      widgets = {

          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'meta_title': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'meta_description': forms.Textarea(attrs={
              'class': INPUT_CLASS,
              "id": "meta_description"
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'text':CKEditor5Widget(
              attrs={'class': 'django_ckeditor_5'},
              config_name='extends'
          )

      }
      
class GalleryCategorySettingsForm(forms.ModelForm):
  
  class Meta:
      model = GalleryCategory
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_title': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_description': forms.Textarea(attrs={
              'class': 'form__controls',
              "id": "meta_description"
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
      }
  
class ProductForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'article': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                "id":"article"
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                "id":"name"
            }),
            'slug': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                "id": "slug"
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASS,
            }),
#             'categories': forms.CheckboxSelectMultiple,
            'manufacturer': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'manufacturer_description': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
             'manufacturer_description': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
            }),
            'sale': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
            }),
            'installment': forms.Textarea(attrs={
                'class': INPUT_CLASS,
            }),
            'quantity': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
            }),
            'quantity_purchase': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
            }),
            'status': forms.CheckboxInput(attrs={
              'class': 'form__controls-checkbox',
            }),
            'meta_h1': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_title': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                "id": "meta_description"
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),

        }

class ProductPropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Название характеристики',
                'id': 'id_char_name',

            }),
            'value': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Значение',
                'id': 'id_char_value'
            }),
        }

# Товар и опции товара
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage

        fields = [
            'parent',
            'src'
        ]
        labels = {
            'src': 'Выбрать изображение'
        }
        widgets = {
            'parent': forms.Select(attrs={
                'class': INPUT_CLASS,
            }),
            'src': CustomImageWidget(),
        }

class PostForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                "id":"name",
                "required": "true"
            }),
            'slug': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                "id":"slug",
                "required": "true"
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASS,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
            }),
            "meta_h1": forms.TextInput(attrs={
              "class":INPUT_CLASS,
            }),
            "meta_h1": forms.TextInput(attrs={
              "class":INPUT_CLASS,
            }),
            "meta_title": forms.TextInput(attrs={
              "class":"form__controls meta_field",
              "id": "meta_title"
            }),
            "meta_description": forms.Textarea(attrs={
              "class":"form__controls meta_field",
              "rows": "5"
            }),
            "meta_keywords": forms.TextInput(attrs={
              "class":INPUT_CLASS,
            }),
            'description': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'},
                config_name='extends'
            )
        }

class BlogCategoryForm(forms.ModelForm):
    """ Form, отвечает за создание категорий постов"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogCategory
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'id':'name'
            }),
            'slug': forms.TextInput(attrs={
              'class': INPUT_CLASS,
              "id": 'slug'
            }),
            'meta_h1': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_title': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),

        }



class CategoryForm(forms.ModelForm):
  """ Form, отвечает за создание категорий и редактирование категорий"""
  class Meta:
    model = Category
    fields = "__all__"
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
          # "placeholder": "Название  категории"
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
        # "placeholder": "Название категори"
      }),
      'add_menu': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      "description": forms.Textarea(attrs={
        "class":"form__controls",
      }),
      "meta_h1": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Заголовок H1"
      }),
      "meta_title": forms.TextInput(attrs={
        "class":"form__controls meta_field",
        "id": "meta_title"
        # "placeholder": "Meta заголовок"
      }),
      "meta_description": forms.Textarea(attrs={
        "class":"form__controls meta_field",
        # "placeholder": "Meta Описание",
        "rows": "5"
      }),
      "meta_keywords": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Meta keywords"
      }),
      'description':CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      # Показывать только корневые категории
      self.fields['parent'].queryset = Category.objects.filter(parent__isnull=True).exclude(id=self.instance.id if self.instance.pk else None)

    
class HomeTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = HomeTemplate
      fields = "__all__"
      widgets = {
          'name': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'meta_title': forms.TextInput(attrs={
              'class': f"{INPUT_CLASS} meta_field",
          }),
          'meta_description': forms.Textarea(attrs={
              'class': f"{INPUT_CLASS} meta_field",
              'rows': 5
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
      }

class ProductionForm(forms.ModelForm):
  class Meta:
      model = Production
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'meta_title': forms.TextInput(attrs={
              'class': f"{INPUT_CLASS} meta_field",
          }),
          'meta_description': forms.Textarea(attrs={
              'class': f"{INPUT_CLASS} meta_field",
              'rows': 5
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'text_sale': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
      }


class ContactTemplateForm(forms.ModelForm):
  """ Form, редактирование страницы контакты"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
      model = ContactTemplate
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'meta_title': forms.TextInput(attrs={
              'class': f"{INPUT_CLASS} meta_field",
          }),
          'meta_description': forms.Textarea(attrs={
              'class': f"{INPUT_CLASS} meta_field",
              'rows': 5
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'activate_page': forms.CheckboxInput(attrs={
            'class': 'form__controls-checkbox',
          }),
      }



class AboutTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
      model = About
      fields = "__all__"
      widgets = {
          'name': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'meta_title': forms.TextInput(attrs={
              'class': f"{INPUT_CLASS} meta_field",
          }),
          'meta_description': forms.Textarea(attrs={
              'class': f"{INPUT_CLASS} meta_field",
              'rows': 5
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'description': CKEditor5Widget(
             attrs={'class': 'django_ckeditor_5'},
             config_name='extends'
         ),
         'description_two': CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        )
      }
           

    
class StockForm(forms.ModelForm):
  """ Form, добавление и редактирование акций"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Stock
    fields = "__all__"
    widgets = {
      'title': forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':INPUT_CLASS,
        "id": "slug"
      }),
      'validity': forms.DateInput(attrs={
        'class':INPUT_CLASS,
      }),
      'description': forms.Textarea(attrs={
        'class': INPUT_CLASS,
        'rows': 5,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'slider_status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'description': CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

class ServicePageForm(forms.ModelForm):
  """ Поля настроек старницы услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = ServicePage
    fields = "__all__"
    widgets = {
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':INPUT_CLASS,
        "id": "slug"
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
              'class': INPUT_CLASS,
            }),
      'meta_description': forms.Textarea(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      })
    }  
    
class ServiceForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Service
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':INPUT_CLASS,
        "id": "slug"
      }),
      'description': forms.Textarea(attrs={
          'class': INPUT_CLASS,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_description': forms.Textarea(attrs={
        'class': INPUT_CLASS,
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'description':CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
      )
    }
    
class SubdomainForm(forms.ModelForm):
  class Meta:
    model = Subdomain
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
        'geotag': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'subdomain': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
    }
    
    
class ColorProductForm(forms.ModelForm):
  class Meta:
    model = ColorProduct
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
        'code_color': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
    }
    
class SubdomainContactForm(forms.ModelForm):
  class Meta:
    model = SubdomainContact
    fields = "__all__"
    widgets = {
        'phone': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
        'phone_two': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'time': forms.DateInput(attrs={
            'class': INPUT_CLASS,
        }),
        'address': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'subdomain': forms.Select(attrs={
            'class': "form__controls-select",
        }),
    }
    
class GalleryForm(forms.ModelForm):
  class Meta:
    model = Gallery
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
    }

class WorksForm(forms.ModelForm):
  class Meta:
    model = Works
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
        'text': CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        )
    }
    
class GalleryCategoryForm(forms.ModelForm):
  class Meta:
    model = GalleryCategory
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
        'slug': forms.TextInput(attrs={
          'class': INPUT_CLASS,
          "id": "slug"
        }),
        'meta_h1': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'meta_title': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'meta_description': forms.Textarea(attrs={
          'class': INPUT_CLASS,
        }),
        'meta_keywords': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
    }

class DeliveryForm(forms.ModelForm):
  class Meta:
    model = Delivery
    fields = "__all__"
    widgets = {
        'meta_h1': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'meta_title': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'meta_description': forms.Textarea(attrs={
          'class': INPUT_CLASS,
        }),
        'meta_keywords': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'description':CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        ),
        'description_two':CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        )
    }

class OfficeForm(forms.ModelForm):
  class Meta:
    model = SalesOffices
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'address': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'phone': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
        'time_work': forms.TextInput(attrs={
          'class': INPUT_CLASS,
        }),
    }
    
    
