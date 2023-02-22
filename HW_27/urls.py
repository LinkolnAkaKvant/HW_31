from django.contrib import admin
from django.urls import path, include

from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('ad/', include('ads.urls')),
    path('user/', include('users.urls'))
]
