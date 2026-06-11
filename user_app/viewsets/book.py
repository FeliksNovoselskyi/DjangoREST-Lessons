import rest_framework.viewsets as viewsets

from rest_framework_simplejwt.authentication import  JWTAuthentication
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from django_filters.rest_framework import DjangoFilterBackend

from user_app.models import Book
from user_app.serializers.book import BookSerializer


# class BookPaginator(PageNumberPagination):
    
#     page_size = 5
#     page_query_param = "page"
#     page_size_query_param = "size"
#     max_page_size = 90
#     last_page_strings = ["last"]


# class BookPaginator(LimitOffsetPagination):
    
#     default_limit = 5
#     max_limit = 30

class BookPaginator(CursorPagination):

    page_size = 2
    
    ordering = "id"
    
    page_size_query_param = "size"



class BookViewset(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPaginator 

    authentication_classes = [
        JWTAuthentication
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filtering_fields = [
        "title"
    ]

    search_fields = [
        "title",
        "author__username"
    ]

    ordering_fields = [
        "published_date"
    ]

    ordering = ["id"]
    