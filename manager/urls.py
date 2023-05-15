from django.urls import path
from .views import department, department_list, department_detail

app_name = "manager"

urlpatterns = [
    path('',department, name="department" ),
    path('department-list/', department_list, name="department-list"),
    path('<int:pk>/department-detail/', department_detail, name="department-detail" )
]