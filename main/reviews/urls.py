from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name="reviews"), 
    path('<slug:slug>/', views.reviews_detail, name="reviews_detail"),
    # path('<slug:slug>/', views.reviews_detail, name="reviews_detail"),
]