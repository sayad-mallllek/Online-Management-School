from django.contrib import admin
from .models import Teacher
from classes.models import Class

# Register your models here.


class ClassesInline(admin.TabularInline):
    model = Class.teachers.through
    extra = 1


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ("first_name", "last_name", "phone", "email")
    inlines = [ClassesInline]
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")
