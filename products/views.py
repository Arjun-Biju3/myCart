from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

def index(request):
    featured_product=Product.objects.order_by('priority')[:4]
    latest_product=Product.objects.order_by('-id')[:8]
    context={
        'featured_product':featured_product,
        'latest_product':latest_product
    }
    return render(request,'index.html',context)

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,8)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'product_layout.html',context)

def detail_product(request,pk):
    product_list=Product.objects.get(pk=pk)
    key=product_list.keyword
    related=Product.objects.filter(title__contains=key).exclude(pk=pk).order_by('-id')[:4]
    context={'product':product_list,'related':related}
    return render(request,'product_details.html',context)


def search(request):
    if request.POST:
        key=request.POST.get('search')
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.filter(title__contains=key)
    product_paginator=Paginator(product_list,8)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'product_layout.html',context)   




