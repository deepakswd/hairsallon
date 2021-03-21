from django.urls import path, include
from rest_framework import routers
from .viewsets import *
from .views import *
# from .viewsets import *

app_name = 'Api '

router = routers.DefaultRouter()
router.register('services', ServiceViewSet, basename='service')
router.register('list-service', ListServicesViewSet, basename='listService')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(),name="login"),
]
