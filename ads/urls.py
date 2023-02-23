from django.urls import path

from ads import views

urlpatterns = [
    path('cat/', views.CategoryListView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDetailView.as_view()),
    path('', views.AdListView.as_view()),
    path('<int:pk>/', views.AdDetailView.as_view()),
    path('create/', views.AdCreateView.as_view()),
    path('<int:pk>/image', views.AdImageView.as_view()),
    path('<int:pk>/update', views.AdUpdateView.as_view()),
    path('<int:pk>/delete', views.AdDetailView.as_view()),
    path('by_user/', views.AuthorAdDetailView.as_view())
]
