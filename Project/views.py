from django.shortcuts import render

# Create your views here.

def getProject(request):
    return render(request, 'project.html')