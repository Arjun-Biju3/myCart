from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def list_products(request):
    return render(request,'product_layout.html')

def detail_product(request):
    return render(request,'product_details.html')

def cart(request):
    return render(request,'cart.html')

def account(request):
    return render(request,'account.html')

