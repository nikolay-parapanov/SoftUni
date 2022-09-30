from random import choice

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, resolve_url

# Create your views here.

# Without render
# def show_departments(request: HttpRequest, *args, **kwargs):
#     print(request.method)
#     print(request.GET)
#     print(request.get_port())
#     print(request.get_host())
#     print(request.get_host())
#     print(request.headers)
#     body = f'path = {request.path},  args= {args}, kwargs= {kwargs}'
#     return HttpResponse(body)


def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        'page_title': 'Departments',
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),

    }
    return render(request, 'departments/all.html', context)

    print(request.method)
    print(request.GET)
    print(request.get_port())
    print(request.get_host())
    print(request.get_host())
    print(request.headers)
    body = f'path = {request.path},  args= {args}, kwargs= {kwargs}'
    return HttpResponse(body)

def show_department_details(request: HttpRequest, department_id):
    body = f'path: {request.path},  id: {department_id}'
    return HttpResponse(body)

def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    return redirect(f'departments/?order_by={order_by}')