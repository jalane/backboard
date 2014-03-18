from django.shortcuts import render

# Create your views here.
def index(request):
    thecode = "return HttpResponse(\"Hello, this is the dyanmic code executor\")"
    
    exec thecode 