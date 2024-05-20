"""
URL configuration for babycare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('userhome', views.userhome),
    path('adminhome', views.adminhome),

    path('wishlist', views.wishlist),
    path('shop', views.shop),
    path('checkout', views.checkout),
    path('contact', views.contact),
    path('empty_contact', views.empty_contact),
    path('about', views.about),
    path('empty_about', views.empty_about),
    path('myaccount', views.myaccount),
    path('viewuser', views.viewuser),
    path('addproduct', views.add_product),
    path('displayproduct', views.display_product),
    path('deleteproduct/<int:d>', views.delete_product),
    path('updateproduct/<int:d>', views.update_details),
    path('logout', views.logout),
    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_pwd,name='reset_password'),
    path('emptycart', views.empty_cart),
    path('emptywishlist', views.empty_wishlist),
    path('addcart/<int:pid>',views.add_cart),
    path('displaycart',views.display_cart),
    path('removefromcart/<int:d>',views.delete_from_cart),
    path('wishlist/<int:d>', views.wishlist),
    path('displaywishlist', views.display_wishlist),
    path('removefromwishlist/<int:d>', views.remove_wishlist),
    path('increment/<int:cart_id>', views.increment_quantity, name="increment_quantity"),
    path('decrement/<int:cart_id>', views.decrement_quantity, name="decrement_quantity"),
    path('newborn',views.newborn,name='newborn'),

    path('babyboy', views.baby_boy, name='baby boy'),
    path('upto6boy', views.upto6_boy, name='3-6M_boy'),
    path('upto9boy', views.upto9_boy, name='6-9M_boy'),
    path('upto12boy', views.upto12_boy, name='9-12M_boy'),
    path('upto18boy', views.upto18_boy, name='12-18M_boy'),
    path('upto24boy', views.upto24_boy, name='18-24M_boy'),

    path('babygirl', views.baby_girl, name='baby girl'),
    path('upto6girl', views.upto6_girl, name='3-6M_girl'),
    path('upto9girl', views.upto9_girl, name='6-9M_girl'),
    path('upto12girl', views.upto12_girl, name='9-12M_girl'),
    path('upto18girl', views.upto18_girl, name='12-18M_girl'),
    path('upto24girl', views.upto24_girl, name='18-24M_girl'),

    path('payment/<int:amount>',views.payment,name='payment'),
    path('deliverydetails/<int:d>', views.delivery_details,name='delivery_details'),
    path('success_page', views.success_page),
    path('update_profile', views.updateprofile),
    path('change_password', views.changepassword),
    path('profile', views.profile, name='profile'),
    path('user_recent_orders', views.user_recentorders, name='user_recent_orders'),
    path('checkout_cart/<int:total>',views.checkout_cart),
    path('payment_cart/<int:l>',views.payment_cart),
    path('payment_success_cart',views.payment_success_cart),
    path('lowstock',views.low_stock),
    path('admin_order_details', views.admin_orders, name='admin_order_details'),
    path('admin_order_update/<int:d>', views.adminorderupdate),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)