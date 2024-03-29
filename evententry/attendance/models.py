from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    college_email = models.EmailField(unique=True)
    roll_no = models.CharField(max_length=13)
    student_number = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=10)
    branch = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    is_hosteler = models.BooleanField(default=False, blank=True)
    is_paid = models.BooleanField(default=False)
    
    is_present_day1 = models.BooleanField(default=False)
    is_present_day2 = models.BooleanField(default=False)
    is_present_day3 = models.BooleanField(default=False)
    is_present_day4 = models.BooleanField(default=False)
    
    timestamp_day1 = models.DateTimeField(null=True, blank=True)
    timestamp_day2 = models.DateTimeField(null=True, blank=True)
    timestamp_day3 = models.DateTimeField(null=True, blank=True)
    timestamp_day4 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} :: {self.roll_no}"