
import rest_framework.serializers as serializers
from django.contrib.auth.models import User

# класс сериализатора для работы с моделями при запросе

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ["id", "username", "password"]
