from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('catpolls/', include('catpolls.urls', namespace='catpolls')),
    path('catblogs/', include('catblogs.urls')),
    path('admin/', admin.site.urls),
    #path('', include('catwork.urls')),
]
