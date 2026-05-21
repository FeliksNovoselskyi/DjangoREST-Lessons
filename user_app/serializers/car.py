
import rest_framework.serializers as serializers
from user_app.models import Car

class CarSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Car
        fields = ["id", "brand"]
        read_only_fields = ["id"]
