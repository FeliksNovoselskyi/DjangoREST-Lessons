from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import rest_framework.viewsets as viewsets
from rest_framework.response import Response
from user_app.serializers.user import UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from user_app.models import Car
from user_app.serializers.car import CarSerializer
from user_app.permissions import IsOwner, IsSuperUser, NotAllowedAny


class CarViewSet(viewsets.ModelViewSet):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    authentication_classes = [
        JWTAuthentication
    ]
    
    
    # lookup_url_kwarg = "car_id"
    
    def get_permissions(self):
        
        if self.action == "retrieve" or self.action == "update":
            return [IsOwner()]
        if self.action == "list":
            return [IsSuperUser()]
        else:
            return [NotAllowedAny()]
    
    # 1
    def retrieve(self, request, pk):
        car = get_object_or_404(Car.objects.all(), pk = pk)
        
        
        
        self.check_object_permissions(request=request, obj=car)
        
        serializer = self.get_serializer(car)
        
        return Response(
            serializer.data
        )
    
    # 2 
    def list(self, request, *args, **kwargs):
        
        self.check_permissions(request=request)
        
        
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            serializer.data
        )
    
    # 3
    # update

    def update(self, request, pk):
        car = get_object_or_404(Car.objects.all(), pk = pk)
        
        self.check_object_permissions(request=request, obj=car)
        
        serializer = self.get_serializer(car, data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            serializer.data
        )
