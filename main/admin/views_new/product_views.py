from django.core.paginator import Paginator
from django.shortcuts import render
from ..forms import ProductForm, ProductImageForm
from admin.services.product_service import get_all_products, get_product_by_id, update_product, save_image_product,create_product

def admin_product(request):
    page = request.GET.get('page', 1)
    products = get_all_products()

    paginator = Paginator(products, 10)
    current_page = paginator.page(int(page))

    context = {
    "items": current_page
    }
    return render(request, "shop/product/product.html", context)

def product_edit(request, pk):
  product = get_product_by_id(pk)
  form = ProductForm(instance=product)
  image_form = ProductImageForm()

  if request.method == 'POST':
    update_product = update_product(request.POST, request.FILES, product)
    if update_product:
      images = request.FILES.getlist('src')
      save_image_product(update_product, images)
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, 'shop/product/product_edit.html', {'form': form_new})

  context = {
  "form":form,
  'image_form': image_form,
  }

  return render(request, "shop/product/product_edit.html", context)

def product_add(request):
    """Добавление нового товара"""
    form = ProductForm()

    if request.method == "POST":
        product = create_product(request.POST, request.FILES)
        if product:
            return redirect('admin_product')  # Успех
        return render(request, "shop/product/product_add.html", {"form": ProductForm(request.POST, request.FILES)})  # Ошибка

    return render(request, 'shop/product/product_add.html', {"form": form})

def product_delete(request,pk):
  product = Product.objects.get(id=pk)
  product.delete()

  return redirect('admin_product')