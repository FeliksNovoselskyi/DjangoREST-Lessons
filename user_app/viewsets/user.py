from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import rest_framework.viewsets as viewsets
from user_app.serializers.user import UserSerializer
from user_app.models import CustomUser
from django.contrib.auth import login, authenticate, logout
from rest_framework.response import Response
from django.template.context_processors import request


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [
        SessionAuthentication
    ]
    permission_classes = [IsAuthenticated]
    

class AuthUserViewSet(viewsets.ViewSet):
    
    permission_classes = [AllowAny]
    
    def create(self, request):
        
        serializer = UserSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
                username = request.data.get('username'), 
                password = request.data.get('password')
            )
        
        if not user:
            return Response(
                data = {
                'message': "credentials validation error"
                },
                status = 401
            )
        
        login(request=request, user = user)

        return Response(
            data = {
                'message': "successfull login"
                },
                status = 200
        )
    
    def destroy(self, request, *args, **kwargs):
        logout(request = request)
        return Response(
            data = {
                'message': "successfull logout"
                },
                status = 200
        )
