from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')


def login_register_page(request):
    return render(request, 'login_register.html')

