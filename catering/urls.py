from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('register/', views.register, name='register'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart' ),
    path('cart/update/<int:cart_id>', views.update_cart, name='update_cart'),
    path('cart/delete/<int:cart_id>', views.delete_cart, name='delete_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order_history/', views.order_history_view, name='order_history'),
    path('manage_products/', views.manage_products, name='manage_products'),
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    
]