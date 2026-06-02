import rest_framework.routers as routers
from .viewsets.user import UserViewSet
from .viewsets.car import CarViewSet
from .api_views.car import CarApiView
from django.urls import path

