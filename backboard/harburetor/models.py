from django.db import models
from django.forms import ModelForm
# Create your models here.

class Har(models.Model):
    DigitalProperty = models.CharField(max_length=511)
    HarContents = models.TextField()
    Description = models.CharField(max_length=511)
    BaseURL = models.CharField(max_length=511)

class HarForm(ModelForm):
    class Meta:
        model = Har
        fields = ['DigitalProperty', 'HarContents', 'Description', 'BaseURL']

    
class HarLine(models.Model):
    HarID = models.ForeignKey(Har)
    RawLine = models.TextField()
    URL = models.CharField(max_length=511)
    RequestHeaders = models.CharField(max_length=1023)
    ResponseHeaders = models.CharField(max_length=1023)
    Cookies = models.CharField(max_length=1023)
    
class Report(models.Model):
	HarID = models.ForeignKey(Har)
	ReportName = models.CharField(max_length=511)
