from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from user_app.models import Car
from user_app.serializers.car import CarSerializer
from user_app.permissions import IsOwner


# 1 APIView - для получение всех объектов Car
class AllCarsApiView(APIView):

    authentication_classes = [
        JWTAuthentication
    ]

    permission_classes = []

    def get(self, request):
        cars = Car.objects.all()

        serializer = CarSerializer(cars, many = True)

        return Response(
            serializer.data
        )
            
# 2 APIView - для получения конкретного объекта Car

class CarApiView(APIView):

    authentication_classes = [
        JWTAuthentication
    ]

    permission_classes = [
        IsOwner
    ]

    def get(self, request, car_id):
        car = get_object_or_404(Car.objects.all(), id = car_id)

        self.check_object_permissions(request = request, obj = car)

        serializer = CarSerializer(car)

        return Response(
            serializer.data
        )
