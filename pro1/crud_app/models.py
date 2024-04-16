from django.db import models


class Tuition(models.Model):
    student_name = models.CharField(max_length=20)
    previous_marks = models.FloatField()
    standard = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    admission_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)