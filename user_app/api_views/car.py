from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

from user_app.permissions import IsOwner
from user_app.models import Car
from user_app.serializers.car import CarSerializer


class CarApiView(APIView):
    
    authentication_classes = [
        JWTAuthentication
    ]
    
    permission_classes = []
    
    def get(self, request):
        
        cars = Car.objects.all()
        
        serializer = CarSerializer(cars, many=True)
        
        return Response(
            serializer.data
        )


class CarObjectApiView(APIView):
    
    authentication_classes = [
        JWTAuthentication
    ]
    
    permission_classes = [
        IsOwner
    ]
    
    def get(self, request, car_id):
        car = get_object_or_404(Car.objects.all(), id = car_id)
        
        self.check_object_permissions(request=request, obj=car)
        
        serializer = CarSerializer(car)
        
        return Response(
            serializer.data
        )
    
    def put(self, request, car_id):
        car = get_object_or_404(Car.objects.all(), id = car_id)
        
        self.check_object_permissions(request=request, obj=car)
        
        serializer = CarSerializer(car, request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            serializer.data
        )
    
    def patch(self, request, car_id):
        car = get_object_or_404(Car.objects.all(), id = car_id)
        
        self.check_object_permissions(request=request, obj=car)

        serializer = CarSerializer(
            car, 
            request.data,
            partial = True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            serializer.data
        )
    
    def delete(self, request, car_id):
        car = get_object_or_404(Car.objects.all(), id = car_id)
        
        self.check_object_permissions(request=request, obj=car)

        car.delete()
        
        return Response(
            {
            "message": "Successful delete"      
            }
        )
