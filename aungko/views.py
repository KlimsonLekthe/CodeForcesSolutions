from django.shortcuts import render

def home(request):
    return render(request, 'aungko/home.html')

def about(request):
    return render(request, 'aungko/about.html')

def contact(request):
    return render(request, 'aungko/contact.html')



