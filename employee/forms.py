from django import forms
from .models import Employee

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'age',
            'department'
        )


   