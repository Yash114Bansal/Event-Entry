from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_number', 'branch', 'is_hosteler']
        
class MarkPresentSerializer(serializers.Serializer):
    student_number = serializers.CharField()
    day = serializers.ChoiceField(choices=['day1', 'day2', 'day3', 'day4'])