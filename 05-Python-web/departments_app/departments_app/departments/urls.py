# Departments's app urls.py
from django.urls import path

from departments_app.departments.views import show_departments, show_department_details, redirect_to_first_department

urlpatterns = (
    # /departments/
    path('', show_departments),
    # /departments/{department_id}/
    path('<department_id>/', show_department_details),
    # /departments/int/{department_id}/
    path('int/<int:department_id>/', show_department_details),

    path('redirect/', redirect_to_first_department)

)