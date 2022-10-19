# admin.py
from django.contrib import admin

from models_demos.web.models import Employee, Department, Project


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):  #
    list_display = ('pk', 'first_name', 'last_name', 'job_level', 'department2')
    list_filter = ['job_level']
    search_fields = ('first_name', 'last_name')

    fieldsets = (
        (
            'Personal Info',
             {
                 'fields': ('first_name', 'last_name'),
              }
        ),
        (
          'Professional Info',
            {
                'fields': ('job_level', 'works_full_time', 'email_address')
            }
        )
    )

    def department2(self, obj):
        return obj.department.name

    # def has_delete_permission(self, request, obj=None):
    #      return False
    # def has_add_permission(self, request):
    #     return False

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
