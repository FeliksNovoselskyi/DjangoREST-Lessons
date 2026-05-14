import rest_framework.routers as routers
from .viewsets.user import UserViewSet, AuthUserViewSet

from rest_framework.authentication import SessionAuthentication

# Router - объект который создает маршруты
router = routers.DefaultRouter()
router.register(
    'users',
    UserViewSet
)
router.register(
    'auth',
    AuthUserViewSet,
    basename="auth"
)
urlpatterns = router.urls

