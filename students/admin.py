from django.contrib import admin
from .models import Student, Guardian

# Register your models here.


class GuardianInline(admin.StackedInline):
    model = Guardian
    fieldsets = (
        (
            "Identity",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Contact",
            {"fields": ("phone", "email")},
        ),
    )
    extra: int = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ("first_name", "last_name", "birth_date", "active_class")
    inlines = [GuardianInline]
