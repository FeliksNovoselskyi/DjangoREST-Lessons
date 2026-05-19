import rest_framework.routers as routers
from .viewsets.user import UserViewSet

from rest_framework.authentication import SessionAuthentication

# Router - объект который создает маршруты
router = routers.DefaultRouter()
router.register(
    'users',
    UserViewSet
)

urlpatterns = router.urls

