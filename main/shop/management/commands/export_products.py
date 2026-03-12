from django.core.management.base import BaseCommand
from openpyxl import Workbook
from shop.models import Product


class Command(BaseCommand):
    help = 'Export Product model data to Excel'

    def handle(self, *args, **kwargs):
        wb = Workbook()
        ws = wb.active
        ws.title = 'Products'

        headers = [
            'Артикул',
            'Название',
            'Slug',
            'Категория',
            'Родительская категория',
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
            'Изображение категории',
            'Описание категории',
            'Meta H1 категории',
            'Meta Title категории',
            'Meta Description категории',
            'Meta Keywords категории',
            'Выводить в меню',
            'Текст скидки popup',
            'Кнопка в карточке товара',
            'Показывать цену',
        ]

        ws.append(headers)

        for product in Product.objects.prefetch_related('category'):

            # берем первую категорию (как ForeignKey)
            category = product.category.first()

            ws.append([
                product.name,
                category.name if category else '',
                category.parent.name if category and category.parent else '',
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

                category.image.url if category and category.image else '',
                category.description if category else '',
                category.meta_h1 if category else '',
                category.meta_title if category else '',
                category.meta_description if category else '',
                category.meta_keywords if category else '',
                'Да' if category and category.add_menu else 'Нет',
                category.sale_text if category else '',
                category.get_name_btn_display() if category else '',
                category.get_view_price_display() if category else '',
            ])

        file_name = 'products_export.xlsx'
        wb.save(file_name)

        self.stdout.write(
            self.style.SUCCESS(f'✔ Файл успешно сохранён как "{file_name}"')
        )