from django.db import models
from school.utils import SoftDeleteModel
import datetime


YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]
CURRENT_YEAR = datetime.date.today().year


class TeacherAcademicYear(SoftDeleteModel):
    # subjects = models.ManyToManyField("subjects.Subject")
    year = models.IntegerField(
        verbose_name=("year"),
        choices=YEAR_CHOICES,
        default=CURRENT_YEAR,
        blank=False,
        null=False,
    )

    pass


class Teacher(SoftDeleteModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
