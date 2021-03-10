from rest_framework import fields, serializers

from .models import Collection, Order, Product, ProductOrder, Review 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 
            'description', 'price', 
            'created_at', 'updated_at'
        ]

    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'user_id', 'position', 
            'status', "total_order_amount",
            'created_at', 'updated_at'
        ]   


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id', 'author_id', 'product_id', 
            'text', "rating",
            'created_at', 'updated_at'
        ]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'id', 'header',  
            'text', "products",
            'created_at', 'updated_at'
        ]