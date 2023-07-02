from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name='home' ),
    path("aboutUs/", views.about),
    path("services/", views.services),
    path("contactUs/", views.contact),
    path("quote/", views.quote),
    path("blog/", views.blog),
    path("feature/", views.features),
    path("orders/", views.order),
    path("price/", views.price),

    
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
