# admin.py
from django.contrib import admin

from models_demos.web.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):  #
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
