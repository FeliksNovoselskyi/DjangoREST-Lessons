import rest_framework.routers as routers
from .api_views import *
from django.urls import path
from user_app.viewsets.book import BookViewSet
from user_app.viewsets.car import CarViewSet

router = routers.DefaultRouter()


router.register(r"cars", CarViewSet)
router.register(r"books", BookViewSet)

# urlpatterns = [
#     path("cars/all/", AllCarsApiView.as_view()),
#     path("cars/<int:car_id>/", CarApiView.as_view())
# ]

urlpatterns = router.urls
