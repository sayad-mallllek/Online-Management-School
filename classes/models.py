from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

GRADE_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

SECTION_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
    ("G", "G"),
    ("H", "H"),
    ("I", "I"),
    ("J", "J"),
    ("K", "K"),
    ("L", "L"),
    ("M", "M"),
    ("N", "N"),
    ("O", "O"),
    ("P", "P"),
    ("Q", "Q"),
    ("R", "R"),
    ("S", "S"),
    ("T", "T"),
    ("U", "U"),
    ("V", "V"),
    ("W", "W"),
    ("X", "X"),
    ("Y", "Y"),
    ("Z", "Z"),
)


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


class Section(SoftDeleteModel):
    name = models.CharField(
        max_length=1, choices=SECTION_CHOICES, verbose_name="Section"
    )

    def __str__(self):
        return self.name


class Grade(SoftDeleteModel):
    name = models.CharField(max_length=2, choices=GRADE_CHOICES, verbose_name="Grade")

    def __str__(self):
        return self.name


class Class(SoftDeleteModel):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    teachers = models.ManyToManyField("teachers.Teacher")

    class Meta:
        unique_together = (
            "grade",
            "section",
        )

    def __str__(self):
        return f"{self.grade} {self.section}"
