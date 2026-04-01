from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('category/<int:id>/', views.category_products, name='category_products'),

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),

    path('search/', views.search_products, name='search_products'),

    path('checkout/', views.checkout, name='checkout'),

    path('orders/', views.order_list, name='order_list'),
    path('order/<int:id>/', views.order_detail, name='order_detail'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]