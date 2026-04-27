from django.urls import path
from .views import students, get_student, update_student, delete_student

urlpatterns = [
    path('students/', students),                 
    path('students/<int:pk>/', get_student),      
    path('students/<int:pk>/update/', update_student),
    path('students/<int:pk>/delete/', delete_student),
]