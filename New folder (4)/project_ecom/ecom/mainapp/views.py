from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def bkash(request):
    n = 'isalam'
    return HttpResponse(f'learn whit {n}')