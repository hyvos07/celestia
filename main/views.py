from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product

# Show the main page
def show_main(request):
    all_products = Product.objects.all()
    
    context = {
        'name': 'Pop Up Parade Figure Furina - Animula Choragi Ver. Genshin Impact',
        'price': 2300000,
        'description': 'This is a description of the product. It is very long and detailed so that it will exceed the maximum length of the field.',
        'stock': 2,
        'chara': 'Furina',
        'game': 'Genshin Impact',
        'category': 'Plush',
        'image_URL' : r'assets\dev\Error.png',
        'price_with_comma': '2,300,000',
        'is_stock_empty': False,
        'all_products': all_products,
    }

    return render(request, "main.html", context)


# Create a new entry of a product
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


# Show all products in XML format
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


# Show all products in JSON format
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# Show a product filtered based on its ID in XML
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


# Show a product filtered based on its ID in JSON
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")