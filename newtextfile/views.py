from django.http import HttpResponse
from django.shortcuts import render

def print_hello(request):
    return render(request,'index.html')


