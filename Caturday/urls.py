from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('homepage.urls', namespace='landing')),
    path('polls/', include('catpolls.urls', namespace='catpolls')),
    path('blogs/', include('catblogs.urls', namespace='catblogs')),
    path('thoth/', include('omnipotenthoth.urls', namespace='thoth')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
