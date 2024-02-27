from rest_framework.decorators import api_view,authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import status
import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

logger = logging.getLogger('mylogger')


@api_view(http_method_names=['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_emp(request):
    if request .method == 'POST':
        try:
            serializer = EmployeeSerializer(data= request.data)
            serializer.is_valid()
            serializer.save()
            logger.info('Employee Is Created')
            return Response(data=serializer.data, status=201)
        except:
            logger.error('This data saved with error')
            return Response(data=serializer.errors, status=400)
        
    if request.method == 'GET':
        try:
            obj = Employee.objects.all()
            serializer = EmployeeSerializer(obj, many = True)
            logger.info('Employee Data Fetched')
            return Response(data=serializer.data, status=200)
        except:
            logger.error('This data fetched with error')
            return Response(data=serializer.errors, status=400)
        
@api_view(http_method_names=['GET','PUT','PATCH','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def details(request, pk):
    obj = get_object_or_404(Employee, pk=pk)
    if request.method == 'GET':
        try:
            serializer = EmployeeSerializer(obj)
            logger.info('Employee data fetched succesfully')
            return Response(data=serializer.data, status=200)
        except:
            logger.error('this data fetched with error')
            return Response(data={'details':'it has some errors'}, status=400)

    if request.method == 'PUT':
        try:
            serializer = EmployeeSerializer(data= request.data, instance=obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Employee data updated succesfully')
            return Response(data=serializer.data, status=200)
        except:
            logger.error('this updated with error')
            return Response(data={'details':'it has some errors'}, status=400)
        
    if request.method == 'DELETE':
        try:
            obj.delete()
            logger.info('Employee deleted succesfully')
            return Response(data=None, status=204)
        except:
            logger.info('employee deleting have some errors')
            return Response(data={'details':'No content'}, status=204)
    
                
