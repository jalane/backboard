from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# Create your views here.
def index(request):
	return HttpResponse("Hello, this is the errorgen index")

"""
Render an error code based on input url
"""
def renderError(request,errorCode):
    return HttpResponse(status=errorCode)
    
