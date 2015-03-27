from django.contrib import admin

# Register your models here.
from myproject.models.user import User
 
 
admin.site.register(User)