from django import forms
from .models import Department

class EmployeeDepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = (
            'department',
        )
