
import rest_framework.serializers as serializers
from user_app.models import CustomUser

# класс сериализатора для работы с моделями при запросе

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password"]
