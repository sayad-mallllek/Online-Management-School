from django.db import models
from school.utils import SoftDeleteModel

# Create your models here.
class Subject(SoftDeleteModel):
    name = models.CharField(max_length=200)
    sub = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    classes = models.ManyToManyField("classes.Class")
    teachers = models.ManyToManyField("teachers.Teacher")

    def __str__(self):
        return f"{self.name} - {self.code}"
