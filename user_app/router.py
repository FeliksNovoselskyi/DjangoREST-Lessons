import rest_framework.routers as routers
from .viewsets.user import UserViewSet
from .viewsets.car import CarViewSet


router = routers.DefaultRouter()
router.register(
    'users',
    UserViewSet
)
router.register("cars", CarViewSet)

urlpatterns = router.urls

