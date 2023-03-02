from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from ads import views
from ads.views import SelectionViewSet
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register("location", LocationViewSet)
router.register("selection", SelectionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.main_page),
    path('ad/', include('ads.urls')),
    path('user/', include('users.urls')),
]

urlpatterns += router.urls
