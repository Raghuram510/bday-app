from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

def wishes(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'wishes.html')