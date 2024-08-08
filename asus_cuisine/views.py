from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def overview(request):
    return render(request,'overview.html')
def achievements(request):
    return render(request,'achievements.html')
def menu(request):
    return render(request,'menu.html')