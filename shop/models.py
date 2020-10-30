from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.shortcuts import reverse

class Seller(models.Model):
    name = models.CharField(default="My Shop", null=False,
                            max_length=30, blank=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, null=False)

    class Meta:
        verbose_name = ("Seller")
        verbose_name_plural = ("Sellers")
        ordering = ['name']
        db_table = 'seller'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Seller_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    name = models.CharField(blank=False, null=False,
                            max_length=40, primary_key=True, unique=True)
    price = models.PositiveIntegerField(
        blank=False, null=False, validators=[MinValueValidator(1)])
    size = models.CharField(default='N.A.', null=False, max_length=20)
    quantity_available = models.PositiveIntegerField(default=0, null=False)
    min_quantity = models.PositiveIntegerField(default=0, null=False)
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="seller_items")

    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")
        ordering = ['name', 'price']
        db_table = 'item'

    def __str__(self):
        return self.name


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = ("Notification")
        verbose_name_plural = ("Notifications")
        ordering = ['-date']
        db_table = 'notification'

    def __str__(self):
        return self.name


class BillItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()


class Bill(models.Model):
    customer = models.CharField(max_length=100)
    dateTime = models.DateTimeField()
    total = models.IntegerField()
    items = models.ManyToManyField(BillItem)
