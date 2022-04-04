from django.db import models


class Collection(models.Model):
    item = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=225)
    birth_date = models.DateField(null=True)


class Order(models.Model):
    PENDING_STATUS = 'P'
    COMPELET_STATUS = 'C'
    FAILED_STATUS = 'F'
    STATUS_PAYMENT = [
        (PENDING_STATUS, 'Pending'),
        (COMPELET_STATUS, 'Complete'),
        (FAILED_STATUS, 'Failed'),
    ]
    placrd_at = models.DateTimeField(auto_now_add=True)
    paymet_status = models.TextField(max_length=1, choices=STATUS_PAYMENT, default=PENDING_STATUS)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255, null=True)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class Cart(models.Model):
    cart = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
