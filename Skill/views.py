from django.shortcuts import render

# Create your views here.

def getSkill(request):
    return render(request, 'skill.html')