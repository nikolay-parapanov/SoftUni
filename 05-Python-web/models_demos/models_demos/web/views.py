from django.shortcuts import render, get_object_or_404, redirect
from django.template import context

from models_demos.web.models import Employee, Department


def index(request):
    # employees = [e for e in Employee.objects.all() if e.id == 1]
    employees2 = Employee.objects.all()

    context = {
        # 'employees': employees,
        'employees2': employees2,
        # 'department': Department.objects.get(pk=1),
    }
    return render(request, 'index.html', context)

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')


def department_details(request, pk):
    context = {
        'deparment': get_object_or_404(pk)
    }

    return render(request, 'department-details.html', context)