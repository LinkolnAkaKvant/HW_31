from django.urls import path
from users import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.CreateView.as_view()),
    path('<int:pk>/update/', views.UserUpdateView.as_view()),
    path('<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('loc/', views.LocationListView.as_view()),
    path('loc/create/', views.LocationCreateView.as_view()),
    path('loc/<int:pk>/', views.LocationDetailView.as_view()),
    path('loc/<int:pk>/delete/', views.LocationDeleteView.as_view()),
]
