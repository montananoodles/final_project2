from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, CustomerProfile, SellerProfile, Service, PicsPosts, Appointment, NextAppointment
from .Serializer import (
    UserProfileSerializer, CustomerProfileSerializer, SellerProfileSerializer,
    ServiceSerializer, PicsPostsSerializer, AppointmentSerializer, NextAppointmentSerializer
)

@api_view(['GET'])
def index(request):
    return Response('Hello, welcome to the API!')

# @api_view(['GET'])
# def getImages(request):
#     res=[] #create an empty list
#     for img in PicsPosts.objects.all(): #run on every row in the table...
#         res.append({"service":img.service,
#                 "description":img.description,
#                "image":str( img.image)
#                 }) #append row by to row to res list
#     return Response(res) #return array as json response


@api_view(['POST'])
def add_userprofile(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerProfileView(APIView):
    # def get(self, request):
    #     res=[] 
    #     for img in PicsPosts.objects.all(): 
    #         res.append({"service":img.service,
    #             "description":img.description,
    #            "image":str( img.image)
    #             }) 
    #     return Response(res)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerProfileView(APIView):
    # def get(self, request):
    #     res=[] 
    #     for img in PicsPosts.objects.all(): 
    #         res.append({"service":img.service,
    #             "description":img.description,
    #            "image":str( img.image)
    #             }) 
    #     return Response(res)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = SellerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_service(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PicsPostsView(APIView):
    def get(self, request):
        res=[] 
        for img in PicsPosts.objects.all(): 
            res.append({"service_type":img.service_type,
                "description":img.description,
               "image":str( img.image)
                }) 
        return Response(res) 

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = PicsPostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def add_appointment(request):
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_nextappointment(request):
    if request.method == 'POST':
        serializer = NextAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
