from django.core.management.base import BaseCommand
from openpyxl import Workbook
from shop.models import Product


class Command(BaseCommand):
    help = 'Export Product model data to Excel'

    def handle(self, *args, **kwargs):
        wb = Workbook()
        ws = wb.active
        ws.title = 'Products'

        # Заголовки
        headers = [
            'ID',
            'Артикул',
            'Название',
            'Slug',
            'Категория',
            'Производитель',
            'Описание производителя',
            'Цвета',
            'Изображение',
            'Цена',
            'Рассрочка',
            'Скидка',
            'Количество',
            'Куплено',
            'Опубликован',
            'Meta H1',
            'Meta Title',
            'Meta Description',
            'Meta Keywords',
            'Обновлено'
        ]

        ws.append(headers)

        # Данные
        for product in Product.objects.all():

            ws.append([
                product.id,
                product.article,
                product.name,
                product.slug,
                product.category.name if product.category else '',
                product.manufacturer,
                product.manufacturer_description,
                product.colors,
                product.image.url if product.image else '',
                product.price,
                product.installment,
                product.sale,
                product.quantity,
                product.quantity_purchase,
                'Да' if product.status else 'Нет',
                product.meta_h1,
                product.meta_title,
                product.meta_description,
                product.meta_keywords,
                product.updated_at.strftime('%Y-%m-%d %H:%M')
            ])

        # Сохранение
        file_name = 'products_export.xlsx'
        wb.save(file_name)

        self.stdout.write(
            self.style.SUCCESS(f'✔ Файл успешно сохранён как "{file_name}"')
        )