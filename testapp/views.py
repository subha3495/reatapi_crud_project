from django.shortcuts import render
from .models import Employee
from .serializers import Employeeserializer
from rest_framework.viewsets import ModelViewSet
class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    # pagination_class = Mypagepagination

