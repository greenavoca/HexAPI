from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.ImageListCreateAPIView.as_view())
]