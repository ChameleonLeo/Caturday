from django.urls import path, include
from . import views

app_name = 'catblogs'

urlpatterns = [
    path('', views.catpost_list, name='catpost_list'),
    path('catpost/', include([
        path('<int:pk>/', views.catpost_detail, name='catpost_detail'),
        path('new/', views.catpost_new, name='catpost_new'),
        path('<int:pk>/edit/', views.catpost_edit, name='catpost_edit'),
    ])),
]
