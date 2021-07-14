from . import views
from django.urls import path
from django.contrib.auth import views as auth_v

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/',  views.get_profile, name='get_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path('login/', auth_v.LoginView.as_view(), name='login'),
    path('logout/', auth_v.LogoutView.as_view(), name='logout'),

    path('password-reset/', auth_v.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_v.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_v.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_v.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password-change/', auth_v.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_v.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
