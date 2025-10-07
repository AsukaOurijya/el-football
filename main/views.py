from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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
        'name' : 'Muhammad Azka Awliya',
        'class' : 'PBP C',
        'product_list' : products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'display_name' : display_name
    }

    return render(request, "main.html", context)

def show_xml(request):
    shop_item = Product.objects.all()
    xml_data = serializers.serialize("xml", shop_item)
    return HttpResponse(xml_data, description_type="application/xml")

def show_json(request):
    product_list = product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.description,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, shop_id):
    shop_item = Product.objects.filter(pk=shop_id)
    xml_data = serializers.serialize("xml", shop_item)
    return HttpResponse(xml_data, description_type="application/xml")

def show_json_by_id(request, product_id):
    try:
        product = product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)

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

    try:
        products.increment_views()
    except Exception:
        pass

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

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request,id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)