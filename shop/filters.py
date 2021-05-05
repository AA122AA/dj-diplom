from django.db.models.query import QuerySet
from django_filters import rest_framework as filters
from django_filters.filters import CharFilter, ChoiceFilter, DateFromToRangeFilter, NumberFilter
from rest_framework import fields

from shop.models import Order, Product, Review, OrderStatusChoices


class OrderFilter(filters.FilterSet):
    """Фильтры для заказов."""

    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()
    status = ChoiceFilter(choices=OrderStatusChoices.choices)

    class Meta:
        model = Order
        fields=("status", "total_order_amount", "created_at", "updated_at", "user_id", "position")

class ProductFilter(filters.FilterSet):
    """Фильтры для товаров."""
    name = CharFilter("name")
    price_g = NumberFilter("price", lookup_expr="gte")
    price_l = NumberFilter("price", lookup_expr="lte")


    class Meta:
        model = Product
        fields=("price", "name")

class ReviewFilter(filters.FilterSet):
    """Фильтры для отзывов."""

    created_at = DateFromToRangeFilter()

    class Meta:
        model = Review
        fields=("author_id", "product_id", "created_at")