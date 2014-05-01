from django.db import models

# Create your models here.
class Person(models.Model): 
    FirstName = models.CharField(max_length=63)
    LastName = models.CharField(max_length=63)
    UserID	= models.CharField(max_length=63)
    
    def __unicode__(self):
        return u'%s. %s' % (self.FirstName[0], self.LastName)
    
        
class DynaScript (models.Model):
    ScriptName = models.CharField(max_length=63)
    ScriptCode = models.TextField()
    ScriptDescription = models.CharField(max_length=1023)
    UserID = models.ForeignKey(Person)
    Created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.ScriptName, self.pk)