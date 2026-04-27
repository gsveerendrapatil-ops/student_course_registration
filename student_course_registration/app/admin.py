from django.contrib import admin

from .models import Course, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("st_name", "st_email", "course_name", "st_active", "admition_date")
    list_filter = ("st_active", "course_name")
    search_fields = ("st_name", "st_email", "course_name__course_name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ("course_name",)
