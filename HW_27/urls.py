from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ads import views
from users.views import LocationViewSet

router = SimpleRouter()
router.register("location", LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.main_page),
    path('ad/', include('ads.urls')),
    path('user/', include('users.urls'))
]

urlpatterns += router.urls
