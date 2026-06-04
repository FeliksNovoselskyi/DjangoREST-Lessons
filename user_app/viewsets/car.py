import rest_framework.viewsets as viewsets
from rest_framework.permissions import AllowAny
from datetime import date

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from user_app.models import Car, Book
from user_app.serializers.car import CarSerializer
from user_app.permissions import IsOwner, IsSuperUser, NotAllowedAny
from django.contrib.auth.models import User


class CarViewSet(viewsets.ModelViewSet):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    authentication_classes = [
        JWTAuthentication
    ]
    
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
        
        # user1 = User.objects.get(id = 1)
        # user2 = User.objects.get(id = 2)
        
        # for i in range(1, 71):
        #     book = Book(
        #         title = f"Book {i}",
        #         author = user1,
        #         published_date = date(2026, 5, 4)
        #     )
        #     book.save()
        
        # for i in range(70, 31):
        #     book = Book(
        #         title = f"Book {i}",
        #         author = user2,
        #         published_date = date(2026, 5, 4)
        #     )
        #     book.save()
        
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
