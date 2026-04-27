from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    ST_ACTIVE_STATUS = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    st_name = models.CharField(max_length=100)
    st_phone = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$",
                message="Phone number must contain exactly 10 digits.",
            )
        ],
    )
    st_email = models.EmailField(unique=True)
    course_name = models.ForeignKey("Course", on_delete=models.CASCADE)
    course_fee = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Course fee must be greater than zero.")
        ]
    )
    admition_date = models.DateField()
    st_photo = models.ImageField(upload_to="student_photo/", null=True, blank=True)
    st_active = models.CharField(
        max_length=10, choices=ST_ACTIVE_STATUS, default="active"
    )

    def __str__(self):
        return self.st_name

    def clean(self):
        super().clean()
        if self.admition_date and self.admition_date > timezone.localdate():
            raise ValidationError(
                {"admition_date": "Admission date cannot be in the future."}
            )


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


@receiver(post_delete, sender=Student)
def delete_student_photo(sender, instance, **kwargs):
    if instance.st_photo:
        instance.st_photo.delete(save=False)
