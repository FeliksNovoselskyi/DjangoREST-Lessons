from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    
    message = "You are not owner of this car"
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user_id == request.user.id:
            return True
        
        return False


class IsSuperUser(BasePermission):
    
    message = "You are not super user"
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        
        return False


class NotAllowedAny(BasePermission):
    
    def has_permission(self, request, view):
        return False
