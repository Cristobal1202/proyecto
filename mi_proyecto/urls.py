from django.contrib import admin
from django.urls import path, include
from mi_app.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include('mi_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
