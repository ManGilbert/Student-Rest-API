from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'age',
        'email',
        'phone',
        'department',
        'registration_number',
        'created_at'
    )

admin.site.register(Student, StudentAdmin)