#main
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('create/product/', views.product_create_view, name='product_create'),
    path('product/update/<int:product_id>/', views.product_update_view, name='product_update')
]
