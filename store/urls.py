from django.urls import path

from .views import (CategoryListApiView,
                    ProductCategoryListApiView,
                    ProductBrandListApiView,
                    ProductBanner,
                    ProductLatest,
                    BrandListApiView,
                    ProductListApiView,
                    ProductRetrieveApiView,
                    NewProductListApiView,
                    SaleProductListApiView)

urlpatterns = [
    path('category/', CategoryListApiView.as_view(), name='category'),
    path('category/<slug:slug>', ProductCategoryListApiView.as_view(), name='product-category'),

    path('brand/', BrandListApiView.as_view(), name='brand'),
    path('brand/<slug:slug>', ProductBrandListApiView.as_view(), name='brand-brand'),

    path('product/', ProductListApiView.as_view(), name='product'),
    path('product/banner', ProductBanner.as_view(), name='product-banner'),
    path('product/latest', ProductLatest.as_view(), name='product-latest'),
    path('product/new-product', NewProductListApiView.as_view(), name='new'),
    path('product/top-sale', SaleProductListApiView.as_view(), name='new'),
    path('product/<slug:slug>', ProductRetrieveApiView.as_view(), name='product-detail'),
]