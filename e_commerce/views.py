from django.shortcuts import render 
from django.http import HttpResponse





def login(request):
    return render(request,"login.html")
def main(request):
    return render (request,"main.html")
def register(request):
    return render (request,"register.html")
def shop(request):
    return render (request,"shop.html")
def electronics(request):
    return render (request,"electronics.html")
def fashion(request):
    return render (request,"fashion.html")
def beauty(request):
    return render (request,"beauty.html")
def groceries(request):
    return render (request,"groceries.html")