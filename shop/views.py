from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .filters import OrderFilter, ProductFilter, ReviewFilter
from .models import Collection, Order, Product, ProductOrder, Review 
from .serializers import *

class ProductViewSet(ModelViewSet):
    """ViewSet для продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class OrderViewSet(ModelViewSet):
    """ViewSet для заказа."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter


class ReviewViewSet(ModelViewSet):
    """ViewSet для отзыва."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter

class CollectionViewSet(ModelViewSet):
    """ViewSet для подборки."""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer