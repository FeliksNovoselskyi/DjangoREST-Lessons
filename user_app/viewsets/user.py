from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import rest_framework.viewsets as viewsets
from user_app.serializers.user import UserSerializer
from user_app.models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [
        JWTAuthentication
    ]
    permission_classes = [IsAuthenticated]
