from django.urls import path
from .views import students, update_student, delete_student

urlpatterns = [
    path('students/', students),
    path('students/<int:pk>/', update_student),
    path('students/<int:pk>/delete/', delete_student),
]