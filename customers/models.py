from django.db import models
from django.contrib.auth.models import User

# model for customer

class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    user=models.OneToOneField(User,related_name='customer_profile',on_delete=models.CASCADE)
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choice=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name