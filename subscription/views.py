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
            print(request.data)
