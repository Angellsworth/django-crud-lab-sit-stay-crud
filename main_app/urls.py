from django.urls import path
from . import views # Import views to connect routes to view functions
from .views import DogCreate

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path('dogs/', views.dog_index, name='dog-index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog-detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dog-create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dog-update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dog-delete'),
]
