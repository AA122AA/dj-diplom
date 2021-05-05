from django.conf import settings
from django.db import models


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
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.FloatField(verbose_name="Цена")


class Review(TimestampFields):
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=("Автор"),
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        Product,
        verbose_name=("Продукт"),
        on_delete=models.CASCADE
        )
    text = models.TextField(verbose_name="Текст", blank=True)
    rating = models.IntegerField(verbose_name="Оценка")


class Order(TimestampFields):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=("Пользователь"),
        on_delete=models.CASCADE,
    )
    position = models.ManyToManyField(
        "Product",
        verbose_name=("Позиции"),
        related_name="orders",
        through="ProductOrder"
        )
    status = models.TextField(
        verbose_name="Статус",
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.NEW
    )
    total_order_amount = models.FloatField(verbose_name="Общая сумма заказа")


class Collection(TimestampFields):
    header = models.CharField(verbose_name="Заголовок", max_length=50)
    text = models.TextField(verbose_name="Текст")
    products = models.ManyToManyField(
        Product,
        verbose_name="Продукты",
        related_name="collection"
    )


class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE
        )
    order = models.ForeignKey(
        Order,
        verbose_name="Заказ",
        related_name="order_product",
        on_delete=models.CASCADE
        )
    amount = models.IntegerField(
        verbose_name="Количество"
        )


