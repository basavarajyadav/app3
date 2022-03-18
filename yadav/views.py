from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dhoni(requerst):
    return HttpResponse('<h1>DHONI IS MR COOL</h1>')
