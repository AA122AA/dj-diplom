from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('product-reviews', ReviewViewSet)
router.register('orders', OrderViewSet)
router.register('product-collections', CollectionViewSet)

urlpatterns = [] + router.urls
