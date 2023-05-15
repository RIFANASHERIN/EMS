from django.shortcuts import render, redirect
from .models import Department
from .forms import EmployeeDepartmentModelForm
from employee.models import Employee

# Create your views here.

def department(request):
    form = EmployeeDepartmentModelForm()
    if request.method == "POST":
        form = EmployeeDepartmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager:department-list")
    context = {
        "form" : form
    }
    return render(request, "manager/department.html", context)

def department_list(request):
    departments = Department.objects.all()
    context = {
        "departments" : departments
    }
    return render(request, "manager/department_list.html", context)


def department_detail(request, pk):
    department = Department.objects.filter(id = pk)
    employees = Employee.objects.filter(department = id)
    context = {
        "employees" : employees
    }
    return render(request, "employee/employee_list.html", context)