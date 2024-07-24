from django.contrib import admin
from django.urls import path, include
from mi_app.views import index  # Asegúrate de importar la vista index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mi_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),  # Añade esta línea para que la raíz del sitio dirija a la vista 'index'
]
