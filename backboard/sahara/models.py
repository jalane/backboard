from django.db import models

# Create your models here.
class DynaScript (db.Model):
    ScriptName = db.StringProperty()
    ScriptCode = db.TextProperty(default=none)
    ScriptDescription = db.StringProperty()
    