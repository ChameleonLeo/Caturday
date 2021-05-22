from django.urls import path
from . import views

app_name = 'catpolls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('popular/', views.PopularView.as_view(), name='popular'),
    path('random/', views.RandomView, name='random'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:catuestion_id>/vote/', views.vote, name="vote"),
]
