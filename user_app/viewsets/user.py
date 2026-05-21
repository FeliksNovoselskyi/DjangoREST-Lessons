from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import rest_framework.viewsets as viewsets
from user_app.serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [
        JWTAuthentication
    ]
    permission_classes = [IsAuthenticated]

# request -> authentication -> middleware -> parser -> viewset -> serializer -> ...


# Avtoria
# Petya
# Gelik 500$ - permission
# Mercedes 500$ - permission
# Audi 1000$ - permission
# BMW
# Suzuki
# Daewoo



# 1 - общие permission (IsAuthenticated, IsAdminUser, AllowAny)
# 2 - объектные permission (ModelObjectPermission, ModelObjectPermissionOrReadOnly)

