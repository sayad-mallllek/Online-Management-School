from django.contrib import admin
from .models import Class, Grade, Section

# Register your models here.


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    fields = ("grade", "section", "teachers")
    filter_horizontal = ("teachers",)
    list_display = ("grade", "section")
    list_filter = ("grade", "section")
    search_fields = ("grade", "section")


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ("name",)
    search_fields = ("name",)
