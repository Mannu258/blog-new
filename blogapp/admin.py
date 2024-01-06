from django.contrib import admin
from .models import blogmodel,UserDetails

# Register your models here.
admin.site.register(blogmodel)
admin.site.register(UserDetails)

