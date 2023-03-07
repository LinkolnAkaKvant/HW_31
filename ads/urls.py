from django.urls import path
from rest_framework.routers import SimpleRouter

from ads import views
from ads.views import AdViewSet

router = SimpleRouter()
router.register("", AdViewSet)

urlpatterns = [
    path('<int:pk>/image', views.AdImageView.as_view()),
    path('by_user/', views.AuthorAdDetailView.as_view()),

]

urlpatterns += router.urls
