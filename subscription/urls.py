from django.urls import path

from subscription.views import subscription_mobile_api_view, subscription_mobile_detail_view

# from subscription.views import MobileView

urlpatterns = [
    #    path('mobile/', MobileView.as_view(), name='mobile_subscriptions'),
    #    path('mobile/<int:id>', MobileView.as_view(), name='mobile_subscriptions_process'),
    path('mobile/', subscription_mobile_api_view, name='mobile_subscriptions'),
    path('mobile/<int:id>/', subscription_mobile_detail_view, name='mobile_subscriptions_detail'),
]
