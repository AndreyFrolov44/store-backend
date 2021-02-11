from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductListSerializer, ProductDetailSerializer, CategorySerializer, BrandSerializer, CartSerializer, CartCreateSerializer, CartItemCreateSerializer
from . models import Product, Category, Cart, CartItem, Brand


class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializer


class ProductBanner(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product = Product.objects.filter(banner=True, available=True)
        return product


class ProductLatest(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product = Product.objects.filter(latest=True, available=True)
        return product


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandListApiView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 20


class ProductCategoryListApiView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        product = Product.objects.filter(category__slug=self.kwargs.get('slug', None), available=True)
        return product


class NewProductListApiView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product = Product.objects.filter(available=True, newProduct=True)
        return product


class SaleProductListApiView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product = Product.objects.filter(available=True).order_by('-sale')[:3]
        return product


class ProductBrandListApiView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product = Product.objects.filter(brand__slug=self.kwargs.get('slug', None), available=True)
        return product


class ProductRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.filter(available=True)
    lookup_field = 'slug'


# class CartRetrieveApiView(generics.RetrieveAPIView):
#     serializer_class = CartSerializer
#     queryset = Cart.objects.all()
#
#
# class CartCreateApiView(generics.CreateAPIView):
#     serializer_class = CartCreateSerializer
#     queryset = Cart.objects.all()
#
#
# class CartItemCreateApiView(generics.CreateAPIView):
#     serializer_class = CartItemCreateSerializer
#     queryset = CartItem.objects.all()
#
#
# class CartItemUpdateApiView(generics.DestroyAPIView):
#     serializer_class = CartItemCreateSerializer
#     queryset = CartItem.objects.all()
