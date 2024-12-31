from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = [ "name", "father_name", "address", "age" ]
    search_fields = ["name"]


admin.site.register(Student, StudentAdmin)
