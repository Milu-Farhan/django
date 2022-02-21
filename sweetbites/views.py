from django.shortcuts import render,redirect
# from .forms import signup
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from .models import Product
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def admin_home(request):
    return render(request, "admin-analytics.html")

def signup(request):
    return render(request, "signup.html")

def signup_auth(request):
    if request.method == "POST":
        print(request.POST)
        print("checkpoint1")
        form = UserCreationForm(request.POST)
        print("checkpoint2")
        print(form)
        if form.is_valid():
            print("checkpoint3")
            user = form.save(commit=False)
            user.username = user.username.lower()
            print("checkpoint4")
            user.save()
            print("checkpoint5")
            return redirect('login')
        else:
            print("checkpoint6")
            return HttpResponse("filed")
    else:
        print("checkpoint7")
        return HttpResponse("filed to validate")
    
def login_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_home')
        else:
            return redirect('home')
    return render(request, "login.html")

def login_auth(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except Exception as e :
            return HttpResponse(str(e))
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.user.is_superuser|request.user.is_staff:
                print(request.user.is_superuser)
                return redirect('admin_home')
            else:
                return redirect('home')
                # return HttpResponse(request.user.is_superuser)
        
        else:
            return HttpResponse( 'Username OR password does not exit')
    else:
        return HttpResponse( 'method error')

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_item(request):
    if request.user.is_superuser:
        if request.method == "POST":
            name= request.POST.get('product_name')
            original_price = request.POST.get('og-price')
            discount_price = request.POST.get('dis-price')
            weight = request.POST.get('weight')
            description = request.POST.get('description')
        
            result = Product.objects.create(name=name,original_price=original_price,discount_price=discount_price,  weight=weight,description=description)
            if result:
                return HttpResponse('ok')
            else:
                return HttpResponse('not ok')
        return render(request, 'admin-add-item.html')
    
    else:
        return redirect('home')

@login_required(login_url='login')
def admin_list(request):
    if request.user.is_superuser:
        items = Product.objects.all()
        return render(request, 'admin-list.html',{'items':items})
    else:
        return redirect('home')

@login_required(login_url='login')
def manage_users(request):
    if request.user.is_superuser:
        users = User.objects.filter(is_superuser=0)
        return render(request, 'manage-users.html',({'users':users}))
    else:
        return redirect('home')

@login_required(login_url='login')
def products(request):
    if request.user.is_superuser:
        items = Product.objects.all()
        return render(request, 'products.html',{'items':items})
    else:
        return redirect('home')