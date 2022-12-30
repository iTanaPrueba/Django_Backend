import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
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
        return Response(mobile_serializer.data, status=status.HTTP_200_OK)
    else:
        if request.method == 'POST':
            mobile_serializer = MobileSerializer(data=request.data)
            if mobile_serializer.is_valid():
                mobile_serializer.save()
                return Response(mobile_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def subscription_mobile_detail_view(request, id=None):
    mobile = Mobile.objects.filter(id=id).first()

    if mobile:
        if request.method == 'GET':
            mobile_serializer = MobileSerializer(mobile)
            return Response(mobile_serializer.data, status=status.HTTP_200_OK)
        else:
            if request.method == 'PUT':
                mobile_serializer = MobileSerializer(mobile, data=request.data)
                if mobile_serializer.is_valid():
                    mobile_serializer.save()
                    return Response(mobile_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                if request.method == 'DELETE':
                    mobile.delete()
                    return Response({'message': "Mobile subscription deleted"}, status=status.HTTP_200_OK)
    else:
        return Response({'message': "Mobile subscription not found"}, status=status.HTTP_400_BAD_REQUEST)
