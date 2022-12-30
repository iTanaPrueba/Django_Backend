import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from subscription.models import Mobile
from subscription.serializers import MobileSerializer


# Create your views here.

# class MobileView(APIView):
#    def get(self, request):
#        mobiles = Mobile.objects.all()
#        mobile_serializer = MobileSerializer(mobiles, many=True)
#        return Response(mobile_serializer.data)

@api_view(['GET', 'POST'])
def subscription_mobile_api_view(request):
    if request.method == 'GET':
        mobiles = Mobile.objects.all()
        mobile_serializer = MobileSerializer(mobiles, many=True)
        return Response(mobile_serializer.data)
    else:
        if request.method == 'POST':
            mobile_serializer = MobileSerializer(data=request.data)
            if mobile_serializer.is_valid():
                mobile_serializer.save()
                return Response(mobile_serializer.data)
            else:
                return Response(mobile_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def subscription_mobile_detail_view(request, id=None):
    if request.method == 'GET':
        mobile = Mobile.objects.filter(id=id).first()
        mobile_serializer = MobileSerializer(mobile)
        return Response(mobile_serializer.data)
    else:
        if request.method == 'PUT':
            mobile = Mobile.objects.filter(id=id).first()
            mobile_serializer = MobileSerializer(mobile, data=request.data)
            if mobile_serializer.is_valid():
                mobile_serializer.save()
                return Response(mobile_serializer.data)
            else:
                return Response(mobile_serializer.errors)
        else:
            if request.method == 'DELETE':
                mobile = Mobile.objects.filter(id=id).first()
                mobile.delete()
                return Response('DELETED')
