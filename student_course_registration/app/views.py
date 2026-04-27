from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm, StudentForm
from .models import Course, Student


def student_list(request):
    students = Student.objects.select_related("course_name").order_by("st_name")
    query = request.GET.get("q", "").strip()
    selected_course = request.GET.get("course", "")
    selected_status = request.GET.get("status", "")

    if query:
        students = students.filter(
            Q(st_name__icontains=query) | Q(course_name__course_name__icontains=query)
        )
    if selected_course:
        students = students.filter(course_name_id=selected_course)
    if selected_status in {"active", "inactive"}:
        students = students.filter(st_active=selected_status)

    paginator = Paginator(students, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "student_list.html",
        {
            "students": page_obj,
            "courses": Course.objects.order_by("course_name"),
            "query": query,
            "selected_course": selected_course,
            "selected_status": selected_status,
        },
    )


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student registered successfully.")
            return redirect("student-list")
    else:
        form = StudentForm()
    return render(
        request,
        "student_form.html",
        {"form": form, "title": "Register Student", "button_text": "Save Student"},
    )


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student record updated successfully.")
            return redirect("student-list")
    else:
        form = StudentForm(instance=student)
    return render(
        request,
        "student_form.html",
        {"form": form, "title": "Update Student", "button_text": "Update Student"},
    )


def student_delete(request, pk):
    student = get_object_or_404(Student.objects.select_related("course_name"), pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student record deleted successfully.")
        return redirect("student-list")
    return render(request, "student_confirm_delete.html", {"student": student})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully.")
            return redirect("course-create")
    else:
        form = CourseForm()
    return render(
        request,
        "course_form.html",
        {"form": form, "title": "Add Course", "button_text": "Save Course"},
    )
