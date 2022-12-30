from django.urls import path

from subscription.views import MobileView

urlpatterns = [
    path('mobile/', MobileView.as_view(), name='mobile_subscriptions'),
    path('mobile/<int:id>', MobileView.as_view(), name='mobile_subscriptions_process'),
]