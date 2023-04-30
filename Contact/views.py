from django.shortcuts import render

# Create your views here.

def getContact(request):
    return render(request, 'contact.html')
