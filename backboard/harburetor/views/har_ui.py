from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader

from harburetor.models import HarForm

#import lxml
def addHar(request):
    #add it all to the template
    if request.method == 'POST':
        form = HarForm(request.POST)
        if form.is_valid():
            #process the form
            return HttpResponseRedirect('/backboard/harburetor/')
    else:
        form = HarForm()
    
    return render(request, 'AddHar.html', {
        'form': form,
    })
