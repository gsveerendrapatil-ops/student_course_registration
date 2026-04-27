from django.urls import path

from . import views

urlpatterns = [
    path("", views.student_list, name="student-list"),
    path("students/", views.student_list, name="student-list-alias"),
    path("add-student/", views.student_create, name="add-student"),
    path("students/add/", views.student_create, name="student-create"),
    path("students/<int:pk>/edit/", views.student_update, name="student-update"),
    path("students/<int:pk>/delete/", views.student_delete, name="student-delete"),
    path("add-course/", views.course_create, name="add-course"),
    path("courses/add/", views.course_create, name="course-create"),
]
