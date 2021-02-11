from rest_framework import serializers

from .models import Category, Brand, Product, ProductImage, ProductSpecification, CartItem, Cart


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = ('name',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        exclude = ('available', 'newProduct', 'topSale', 'description', 'related_products', 'banner', 'latest',)


class ProductDetailSerializer(serializers.ModelSerializer):
    specification = SpecificationSerializer(many=True)
    images = ImageSerializer(many=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)
    related_products = ProductListSerializer(many=True)

    class Meta:
        model = Product
        exclude = ('available', 'newProduct', 'topSale',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    food = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = CartItem
        exclude = ('cart',)


class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class CartCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'
