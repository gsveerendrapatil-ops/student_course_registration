from django import forms

from .models import Course, Student


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.setdefault("class", "form-select")
            else:
                field.widget.attrs.setdefault("class", "form-control")


class StudentForm(BootstrapModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "st_name": "Student Name",
            "st_phone": "Phone Number",
            "st_email": "Email Address",
            "course_name": "Course Name",
            "course_fee": "Course Fee",
            "admition_date": "Admission Date",
            "st_photo": "Profile Photo",
            "st_active": "Status",
        }
        widgets = {
            "admition_date": forms.DateInput(attrs={"type": "date"}),
        }


class CourseForm(BootstrapModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {"course_name": "Course Name"}
