from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Categories")


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    sale = models.PositiveIntegerField(blank=True, null=True)
    priceSale = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    image = models.ImageField(upload_to='product')
    available = models.BooleanField(default=True)
    newProduct = models.BooleanField(default=False)
    topSale = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=400)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specification')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image


class Cart(models.Model):
    phone_number = models.CharField(max_length=12)
    active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.phone_number


class CartItem(models.Model):
    food = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    order_date = models.DateTimeField(auto_now_add=True)
