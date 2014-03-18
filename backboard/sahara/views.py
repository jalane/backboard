from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    thecode = "return HttpResponse('Hello, this is the dyanmic code executor')"
    exec thecode 