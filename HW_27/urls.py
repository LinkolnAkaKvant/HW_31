
from django.contrib import admin
from django.urls import path

from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('cat/', views.CategoryListCreateView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('ad/', views.AdListCreateView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),

]
