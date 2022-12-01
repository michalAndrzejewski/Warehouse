import csv
from django.http import HttpResponse
from app.models import Product


def product_csv(request):

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="products.csv"'}
    )
    writer = csv.writer(response)
    products = Product.objects.all()

    for product in products:

        writer.writerow([product.product_name, product.category, product.unit_price, product.units_in_stock])

    return response
