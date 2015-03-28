from django.contrib import admin

# Register your models here.
from myproject.models.user import User
from myproject.models.ratedmodel import RatedModel
from myproject.models.ratedmodel import RatedObject
from myproject.models.ratedmodel import Attribute
 
 
admin.site.register(User)
admin.site.register(RatedModel)
admin.site.register(RatedObject)
admin.site.register(Attribute)