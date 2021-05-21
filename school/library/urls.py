from django.urls import path, include
from .views import HomeView, search, student

app_name = 'library'

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('search/',search, name = 'search'),
    path('student/<int:sid>', student, name = 'student'),
]
