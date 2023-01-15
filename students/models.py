from django.db import models

# Create your models here.


class SoftDeleteModel(models.Model):

    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


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
