from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import rest_framework.viewsets as viewsets
from user_app.serializers.user import UserSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from user_app.models import Car
from user_app.serializers.car import CarSerializer
from user_app.permissions import IsOwner


class CarViewSet(viewsets.ModelViewSet):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    authentication_classes = [
        JWTAuthentication
    ]
    
    # lookup_url_kwarg = "car_id"
    
    permission_classes = [IsOwner]
    
    def retrieve(self, request, pk):
        car = Car.objects.filter(id=pk)
        
        self.check_object_permissions(request=request, car=car)
        

