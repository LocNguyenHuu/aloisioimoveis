from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def rent(request):
    return render(request, 'rent.html')


def buy(request):
    return render(request, 'buy.html')


def search(request):
    return render(request, 'search.html')


def company(request):
    return render(request, 'company.html')


def contact(request):
    return render(request, 'contact.html')
