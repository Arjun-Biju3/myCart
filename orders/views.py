from django.shortcuts import render,redirect
from .  models import Order,OrderedItem
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
from customers.models import DeliveryAddress


def cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def remove_item(requset,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        user=request.user
        customer=user.customer_profile
        total_price=float(request.POST.get('total'))
        delivery=DeliveryAddress.objects.get(owner=customer)
        delivery.fname=fname
        delivery.lname=lname
        delivery.email=email
        delivery.phone=phone
        delivery.address=address
        delivery.city=city
        delivery.state=state
        delivery.pincode=pincode
        delivery.save()
        order_obj=Order.objects.get(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        if order_obj:
            order_obj.order_status=Order.OREDER_CONFIRMED
            order_obj.total=total_price
            order_obj.save()
            status_message="your order is processed."
            messages.success(request,status_message)
        else:
            status_message="unable to proceed.cart is empty."
            messages.error(request,status_message)
    return redirect('orders')

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity= ordered_item.quantity+quantity
            ordered_item.save()
            
    return redirect('cart')
    
   
@login_required(login_url='account')    
def view_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE) 
    context={'orders':all_orders}
    return render(request,'orders.html',context)
        
def payment(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        delivery,created=DeliveryAddress.objects.get_or_create(owner=customer)
        total_price=float(request.POST.get('total'))
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        
        context={'total':total_price,'cart':cart_obj,'delivery':delivery}
    return render(request,'payment.html',context)
 
    
def cancel_order(request,pk):
    order_obj=Order.objects.get(pk=pk)
    if order_obj.order_status ==Order.ORDER_DELIVERED:
        status_message="Order is already delivered"
        messages.error(request,status_message)
    else:
        order_obj.delete()
        status_message="order cancelled succesfully"
        messages.success(request,status_message)
    return redirect('orders')
    
        