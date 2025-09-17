from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product

# Create your views here.

def show_main(request):
    products = Product.objects.all()
    context = {
        'npm': '2406431510',
        'name' : ' Muhammad Azka Awliya',
        'class' : 'PBP C',
        'products' : products,
    }

    return render(request, "main.html", context)

def show_xml(request):
    shop_item = Product.objects.all()
    xml_data = serializers.serialize("xml", shop_item)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    shop_item = Product.objects.all()
    json_data = serializers.serialize("json", shop_item)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, shop_id):
    shop_item = Product.objects.filter(pk=shop_id)
    xml_data = serializers.serialize("xml", shop_item)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, shop_id):
    shop_item = Product.objects.filter(pk=shop_id)
    json_data = serializers.serialize("json", shop_item)
    return HttpResponse(json_data, content_type="application/json")

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form' : form}
    return render(request, "addpro.html", context)

def show_product(request, id):
    products = get_object_or_404(Product, pk=id)
    products.increment_views()

    context = {
        'products' : products,
    }

    return render(request, "product_detail.html", context)