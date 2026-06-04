import rest_framework.viewsets as viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from user_app.models import Book
from user_app.serializers.book import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    authentication_classes = [
        JWTAuthentication
    ]
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering
    filterset_fields = [
        "title",
        "author"
    ]
    
    # Searching
    search_fields = [
        "title",
        "author__username"
    ]
    
    # Ordering
    ordering_fields = [
        "published_date"
    ]
    ordering = ["title"] # Поля, которое стандартно будет использоваться для фильтрации
