from django.shortcuts import render, redirect
from .models import Employee
from manager.models import Department
from .forms import EmployeeModelForm

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    context = {
        "employees" : employees
    }
    return render(request, "employee/employee_list.html", context)

def employee_detail(request, pk):
    employees = Employee.objects.get(id = pk)
    context = {
        "employees" : employees
    }
    return render(request, "employee/employee_details.html", context)


def employee_create(request):
    form = EmployeeModelForm()
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager:department-list")
    context = {
        "form" : form
    }
    return render(request, "employee/employee_create.html", context)


def employee_update(request, pk):
    employees = Employee.objects.get(id = pk)
    form = EmployeeModelForm(instance=employees)
    if request.method == "POST":
        form = EmployeeModelForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect("/employee")
    context = {
        "employees" : employees,
        "form" : form
    }
    return render(request, "employee/employee_update.html", context)


def employee_delete(request, pk):
    employees = Employee.objects.get(id=pk)
    employees.delete()
    return redirect("/employee")







