from django.shortcuts import render
from django.http import HttpResponse
from sahara.models import DynaScript
import os

# Create your views here.
def index(request):
    thecode = """
op = 'this is a test output'
response = HttpResponse(op)
response['Cache-Control']='max-age:3s'
"""
    
    exec thecode
    return response

def runScript(request, scriptID):
    dc = DynaScript.objects.get(pk=scriptID)
    #try:
    exec dc.ScriptCode.replace('\r\n','\n')
    #except:
    response = HttpResponse("Error: {0}<br/>".format(dc.ScriptCode))
    return response
    
def getESI(request, scriptID, debug="no"):
    dc = DynaScript.objects.get(pk=scriptID)
    if(debug == 'debug'):
        response = HttpResponse("<esi:debug />{0}".format(dc.ScriptCode))
    else:
        response = HttpResponse(dc.ScriptCode)
    return response