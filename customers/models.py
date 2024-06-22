from django.db import models
from django.contrib.auth.models import User

# model for customer

    
class DeliveryAddress(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=10)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address=models.TextField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    

class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    user=models.OneToOneField(User,related_name='customer_profile',on_delete=models.CASCADE)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    delivery_address=models.ForeignKey(DeliveryAddress,related_name='delivery_address',on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username
    

 