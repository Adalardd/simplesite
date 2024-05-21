from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('bboard/', include('bboard.urls')), # Включение маршрутов из приложения 'bboard'
    path('admin/', admin.site.urls),
]


