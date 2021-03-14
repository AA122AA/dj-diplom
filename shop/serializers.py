from typing import OrderedDict
from django.db import models
from rest_framework import fields, serializers

from .models import Collection, Order, Product, ProductOrder, Review 


class ProductOrderaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOrder
        fields = [
            'id', 'product', 
            'amount'
        ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'name', 
            'description', 'price', 
            'created_at', 'updated_at'
        ]

    
class OrderSerializer(serializers.ModelSerializer):

    position = ProductOrderaSerializer(many=True, source="order_product")

    class Meta:
        model = Order
        fields = [
            'id', 'user_id', 'position', 
            'status', "total_order_amount",
            'created_at', 'updated_at'
        ]   
    
    def create(self, validated_data):
        positions = validated_data.pop("order_product")
        _order = super().create(validated_data)
        if positions:
            to_save=[]
            for p in positions:
                to_save.append(ProductOrder(
                    product=p["product"],
                    order=_order,
                    amount=p["amount"]
                ))
            ProductOrder.objects.bulk_create(to_save)
        return _order

    def validate(selfa, attrs:OrderedDict):
        print(type(attrs))
        price = attrs.get("order_product")[0].get("product").price
        amount = attrs.get("order_product").pop().get("amount")
        if attrs.get("total_order_amount") != price*amount:
            raise serializers.ValidationError("Не верно указана общая цена заказа")
        return attrs

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