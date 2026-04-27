from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_student_course_fee_alter_student_st_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="st_photo",
        ),
    ]
