import tempfile
from pathlib import Path

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from .models import Course, Student


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class StudentPhotoDeletionTests(TestCase):
    def test_student_photo_file_is_deleted_when_student_is_deleted(self):
        course = Course.objects.create(course_name="Science")
        photo = SimpleUploadedFile(
            "student-photo.jpg", b"photo-bytes", content_type="image/jpeg"
        )

        student = Student.objects.create(
            st_name="Test Student",
            st_phone="9876543210",
            st_email="test@example.com",
            course_name=course,
            course_fee=1000,
            admition_date="2026-04-25",
            st_photo=photo,
            st_active="active",
        )

        photo_path = Path(student.st_photo.path)
        self.assertTrue(photo_path.exists())

        student.delete()

        self.assertFalse(photo_path.exists())
