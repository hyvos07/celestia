import datetime

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

from main.forms import ProductForm
from main.models import Product
from main.utils.utils import time_ago


# Account Register
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


# User Login
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
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)


# User Logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


# Show the main page
@login_required(login_url='/login')
def show_main(request):
    context = {
        'username': request.user.username,
        'last_login': time_ago(request.COOKIES.get('last_login')),
    }

    return render(request, "main.html", context)


# Create a new entry of a product
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


# Add a product using AJAX
@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    stock = strip_tags(request.POST.get("stock"))
    chara = strip_tags(request.POST.get("chara"))
    game = strip_tags(request.POST.get("game"))
    category = strip_tags(request.POST.get("category"))
    image = strip_tags(request.POST.get("image"))
    
    # Check if any of the fields are empty
    if not name or not price or not description or not stock or not chara or not game or not category or not image:
        return HttpResponse(b"Missing required fields", status=400)
    
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        stock=stock,
        chara=chara,
        game=game,
        category=category,
        image=image,
        user=user
    )
    
    new_product.save()

    return HttpResponse(b"Successfully Created", status=201)


# Edit a product entry
def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)


# Delete a product entry
def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


# Show all products in XML format
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


# Show all products in JSON format
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# Show a product filtered based on its ID in XML
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


# Show a product filtered based on its ID in JSON
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")