from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio-details.html//App1', views.wish),
    path('portfolio-details.html//Web3', views.wish),
    path('portfolio-details.html//App2', views.wish),
    path('portfolio-details.html//Card2', views.wish),
    path('portfolio-details.html//Web2', views.wish),
    path('portfolio-details.html//App3', views.wish),
    path('portfolio-details.html//Card1', views.wish),
    path('portfolio-details.html//Card3', views.wish),
    path('portfolio-details.html//Web3', views.wish),
    path('', views.welcome),
    path('done.html/', views.done)
]