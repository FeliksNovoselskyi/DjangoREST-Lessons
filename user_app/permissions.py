from rest_framework.permissions import BasePermission

from .models import Car

class IsOwner(BasePermission):
    
    # 1
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
        return False
    
    # 2
    def has_object_permission(self, request, view, obj):
        
        if request.user.id == obj.user_id:
            return True
        
        return False
