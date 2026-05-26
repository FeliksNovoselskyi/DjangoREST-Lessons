

import rest_framework.serializers as serializers
from user_app.models import Car

class CarSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        
        if attrs["brand"] == "Mercedes":
            raise serializers.ValidationError("YOu can't create mercedes")
        
        return attrs
    
    class Meta:
        model = Car
        fields = ["id", "brand"]
        read_only_fields = ["id"]
