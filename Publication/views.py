from django.shortcuts import render

# Create your views here.

def getPublication(request):
    return render(request, 'publication.html')