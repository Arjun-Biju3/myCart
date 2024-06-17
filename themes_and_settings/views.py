from django.shortcuts import render



def about_us(request):
    return render(request,'aboutus.html')
 
def contact(request):
    return render(request,'contact.html')
