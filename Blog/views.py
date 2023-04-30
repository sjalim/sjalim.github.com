from django.shortcuts import render

# Create your views here.

def getBlog(request):

    return render(request, 'blog.html')