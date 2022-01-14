from django.contrib import admin

# Register your models here.
from .models import CustomUser


from .models import *



admin.site.register(CustomUser)
admin.site.register(blog)


