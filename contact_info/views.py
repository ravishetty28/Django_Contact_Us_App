from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Contact
# Create your views here.

def home(request):
    if request.method=="POST":
        contact = Contact()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        pin = request.POST.get('pin')

        contact.first_name=first_name
        contact.last_name=last_name
        contact.email=email
        contact.phone_number=phone_number
        contact.address=address
        contact.pin=pin
        contact.save()
        return HttpResponse('<h1>Thanks For Providing Your Information</h1>')
    return render(request, 'home.html')
    