from django.contrib import admin


# Register your models here.
from .models import AssignmentsUpload,AssignmentsSubmit
admin.site.register(AssignmentsUpload)
admin.site.register(AssignmentsSubmit)

