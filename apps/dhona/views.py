from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'web/index.html')
    #return HttpResponse('hello django')

def dashboard(request):
    return render (request, 'dashboard/dashboard.jinja')
