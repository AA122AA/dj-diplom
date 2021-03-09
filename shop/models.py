from django.conf import settings
from django.db import models

# Create your models here.

class OrderStatusChoices(models.TextChoices):

    NEW = "NEW", "Новый"
    IN_PROGRESS = "IN_PROGRESS", "В работе"
    DONE = "DONE", "Закрыт"


class TimestampFields(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Создано в ",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Обновлено в ",
        auto_now=True
    )
    
    class Meta:
        abstract = True


class Product(TimestampFields):
    name = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")


class Review(TimestampFields):
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=("Автор"),
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=("Продукт"),
        on_delete=models.CASCADE
        )
    text = models.TextField(verbose_name="Текст")
    rating = models.IntegerField(verbose_name="Оценка")


class Order(TimestampFields):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=("Пользователь"),
        on_delete=models.CASCADE,
    )
#Понять чтотакое позиции
    status = models.TextField(
        verbose_name="Статус",
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.NEW
    )
    total_order_amount = models.FloatField(verbose_name="Общая сумма заказа")

class Collection(TimestampFields):
    header = models.CharField(verbose_name="Заголовок", max_length=50)
    text = models.TextField(verbose_name="Текст")
    #Разобраться с m2m
    products = models.ManyToManyField(Product)



