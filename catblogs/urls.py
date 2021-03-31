from django.urls import path
from . import views


urlpatterns = [
    path('', views.catpost_list, name='catpost_list'),
    path('catpost/<int:pk>/', views.catpost_detail, name='catpost_detail'),
    path('catpost/new/', views.catpost_new, name='catpost_new'),
    path('catpost/<int:pk>/edit/', views.catpost_edit, name='catpost_edit'),
]
