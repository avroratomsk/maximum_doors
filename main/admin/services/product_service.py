from shop.models import Product
from ..forms import ProductForm, ProductImageForm

def get_all_products():
  return Product.objects.all()

def get_product_by_id(pk):
  return Product.objects.get(id=pk)

def update_product(product, files, data):
  form = ProductForm(data, files, instance=product)
  if form.is_valid():
    form.save()
    return form.instance
  return None

def save_image_product(product, images):
  for image in images:
    ProductImages.objects.create(parent=product, src=image)


def create_product(data, files):
  form = ProductForm(data, files)

  if form.is_valid():
    return form.save()

  return None