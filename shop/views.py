from rest_framework.viewsets import ModelViewSet

from .models import Collection, Order, Product, ProductOrder, Review 
from .serializers import *

class ProductViewSet(ModelViewSet):
    """ViewSet для продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
    """ViewSet для заказа."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(ModelViewSet):
    """ViewSet для отзыва."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CollectionViewSet(ModelViewSet):
    """ViewSet для подборки."""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer