from django.urls import path

from .views import (CategoryListApiView,
                    ProductCategoryListApiView,
                    ProductBrandListApiView,
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

    path('new-product/', NewProductListApiView.as_view(), name='new'),
    path('top-sale/', SaleProductListApiView.as_view(), name='new'),

    path('product/', ProductListApiView.as_view(), name='product'),
    path('product/<slug:slug>', ProductRetrieveApiView.as_view(), name='product-detail'),
]