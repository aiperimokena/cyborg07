#main
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('create/product/', views.product_create_view, name='product_create'),
    path('product/update/<int:product_id>/', views.product_update_view, name='product_update'),
    path('rating/create/<int:product_id>/', views.rating_create_view, name='rating_create'),
    path('rating/answer/create/<int:rating_id>/', views.rating_answer_create_view, name='rating_answer_create'),
    path('profile/', views.user_pofile_view, name='user_pofile'),

    path('payment/<int:product_id>/payment/create/<int:product_quantity>/', views.product_payment_create_view, name='product_payment')
]
