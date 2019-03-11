from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return render(request, 'one.html')