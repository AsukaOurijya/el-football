from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all") 
    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    full_name = request.user.get_full_name()
    display_name = full_name if full_name.strip() else request.user.username

    context = {
        'npm': '2406431510',
        'name' : display_name,
        'class' : 'PBP C',
        'products' : products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
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

def show_json_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "Authentication required."
        }, status=401)

    shop_item = Product.objects.filter(user=request.user)
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
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {
        'form' : form
    }

    return render(request, "addpro.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    products = get_object_or_404(Product, pk=id)
    products.increment_views()

    context = {
        'products' : products,
    }

    return render(request, "product_detail.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def create_product_flutter(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "Authentication required."
        }, status=401)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            "status": False,
            "message": "Invalid JSON payload."
        }, status=400)

    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    thumbnail = data.get('thumbnail', '')
    category = data.get('category') or 'baju'
    is_featured = data.get('is_featured', False)

    if not name or price is None or description is None:
        return JsonResponse({
            "status": False,
            "message": "Name, price, and description are required."
        }, status=400)

    try:
        price = int(price)
    except (TypeError, ValueError):
        return JsonResponse({
            "status": False,
            "message": "Price must be a number."
        }, status=400)

    valid_categories = {choice[0] for choice in Product.CATEGORY_CHOICES}
    if category not in valid_categories:
        category = next(iter(valid_categories))

    product = Product.objects.create(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        user=request.user
    )

    return JsonResponse({
        "status": True,
        "message": "Product created successfully.",
        "id": str(product.id)
    }, status=201)

