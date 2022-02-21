from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup,name='signup'),
    path('signup_auth/',views.signup_auth,name='signup_auth'),
    path('login/',views.login_page,name='login'),
    path('login_auth/',views.login_auth,name='login_auth'),
    path('logout/',views.logout_page,name='logout'),
    path('additem/',views.add_item,name='add_item'),
    path('admin-home/',views.admin_home,name='admin_home'),
    path('admin-list/',views.admin_list,name='admin_list'),
    path('manage_users/',views.manage_users,name='manage_users'),
    path('products/',views.products,name='products')
]