from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


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
    path("detail/", views.blogDetail),
    path('logout/', LogoutView.as_view()),
    
    
]
