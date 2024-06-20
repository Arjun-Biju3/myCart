from django.shortcuts import render,redirect
from .  models import Order,OrderedItem
from django.contrib import messages
from products.models import Product

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
            user=request.user
            customer=user.customer_profile
            total_price=float(request.POST.get('total'))
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
    return redirect('cart')

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
    
    

        
