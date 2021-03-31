from django.urls import path
from . import views

app_name = 'catpolls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:catuestion_id>/', views.detail, name="detail"),
    path('<int:catuestion_id>/results/', views.results, name="results"),
    path('<int:catuestion_id>/vote/', views.vote, name="vote"),
]
