from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

#import lxml
def index(request):
    #add it all to the template
    t = loader.get_template('index.html')
    c = Context({
        'userid' : 'jalane'
    })
    
    response = HttpResponse(t.render(c))
    response['Access-Control-Allow-Origin'] = '*'
    return response
