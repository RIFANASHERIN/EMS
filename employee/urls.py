from django.urls import path
from .views import employee_list, employee_detail, employee_create, employee_update, employee_delete

app_name = "employee"

urlpatterns = [
    path('<int:pk>/', employee_list, name="employee-list"),
    path('<int:pk>/', employee_detail, name="employee-detail"),
    path('create/', employee_create, name="employee-create"),
    path('<int:pk>/update/', employee_update, name="employee-update"),
    path('<int:pk>/delete/', employee_delete, name="employee-delete")
]