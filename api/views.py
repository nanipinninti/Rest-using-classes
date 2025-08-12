from django.shortcuts import render
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics,mixins
# Create your views here.

class EmployeeView(APIView):
    def get(self,req):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True )
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,req):
        serializer = EmployeeSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetailsView(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self,req,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,req,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,req,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response("Succesully deleted",status=status.HTTP_204_NO_CONTENT)

class EmployeeViewUSingGenerics(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,req):
        return self.list(req)

    def post(self,req):
        return self.create(req)
    

class EmployeeDetailsUsingGenerics(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,req,pk):
        return self.retrieve(req,pk)
    def put(self,req,pk):
        return self.update(req,pk)
    def delete(self,req,pk):
        return self.destroy(req,pk)
    