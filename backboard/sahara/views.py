from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    module = imp.new_module('mymodule')
    
    thecode = """
    return HttpResponse("Hello, this is the dyanmic code executor")
    """
    
    exec thecode in module.__dict__

    application = webapp.WSGIApplication([('/', module.MainHandler)], debug=True)
    util.run_wsgi_app(application)