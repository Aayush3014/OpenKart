from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "shop/index.html")

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact page")
    # return render(request, "shop/index.html")

def track(request):
    return HttpResponse("Tracking page")
    # return render(request, "shop/index.html")

def search(request):
    return HttpResponse("search page")
    # return render(request, "shop/index.html")

def prodview(request):
    return HttpResponse("prodview page")
    # return render(request, "shop/index.html")

def checkout(request):
    return HttpResponse("checkout page")
    # return render(request, "shop/index.html")