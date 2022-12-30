import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions

from subscription.models import Mobile


# Create your views here.

class MobileView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            mobiles = list(Mobile.objects.filter(id=id).values())
            if len(mobiles) > 0:
                mobile = mobiles[0]
                message = {'message': "Success", "mobiles:": mobile}
            else:
                message = {'message': "Companies not found ..."}
        else:
            mobiles = list(Mobile.objects.values())
            # permission = [permissions.AllowAny]
            if len(mobiles) > 0:
                message = {'message': "Success", "mobiles:": mobiles}
            else:
                message = {'message': "Mobiles not found..."}

        return JsonResponse(message)

    def post(self, request):
        jd = json.loads(request.body)
        Mobile.objects.create(month=jd['month'], network=jd['network'], plan=jd['plan'],
                              subscriptions=jd['subscriptions'])
        message = {'message': 'Success'}
        return JsonResponse(message)

    def put(self, request, id):
        jd = json.loads(request.body)
        mobiles = list(Mobile.objects.filter(id=id).values())
        if len(mobiles) > 0:
            mobile = Mobile.objects.get(id=id)
            mobile.month = jd['month']
            mobile.network = jd['network']
            mobile.plan = jd['plan']
            mobile.subscriptions = jd['subscriptions']
            mobile.save()
            message = {'message': "Success"}
        else:
            message = {'message': "Company not found"}
        return JsonResponse(message)

    def delete(self, request, id):
        mobiles = list(Mobile.objects.filter(id=id).values())
        if len(mobiles) > 0:
            Mobile.objects.filter(id=id).delete()
            message = {'message': "Success"}
        else:
            message = {'message': "Company not found..."}

        return JsonResponse(message)
