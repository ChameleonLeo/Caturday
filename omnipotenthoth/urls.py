from django.urls import path
from . import views

app_name = 'thoth'

urlpatterns = [
    path('', views.tip_start, name='tip_start'),
    path('tip/', views.tip_next, name="tip_next"),
]
