from django.shortcuts import render

# Create your views here.

def getEducation(request):
    return render(request, 'education.html')