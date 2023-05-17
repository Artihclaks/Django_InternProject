from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from backend.models import Customer
from .serializer import CustomerSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    data = Customer.objects.all()
    serial = CustomerSerializer(data, many=True)
    return Response(serial.data)
    
@api_view(['GET'])
def getRoute(request,pk):
    data1 = Customer.objects.get(part_no=pk)
    serial = CustomerSerializer(data1, many=False)
    return Response(serial.data)
