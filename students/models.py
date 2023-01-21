from django.db import models
from school.utils import SoftDeleteModel

# Create your models here.


class Guardian(SoftDeleteModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)


class Student(SoftDeleteModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    active_class = models.ForeignKey(
        "classes.Class", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
