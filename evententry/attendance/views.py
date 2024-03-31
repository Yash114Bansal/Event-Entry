from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Student, ActiveDay
from .serializers import StudentSerializer,MarkPresentSerializer

class MarkPresentView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = MarkPresentSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        student_number=validated_data['student_number']
        day = validated_data['day']
        student = get_object_or_404(Student, student_number=student_number)

        # Check if student exists
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if fees is paid
        if not student.is_paid:
            return Response({"error": "Fees not paid"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if day is valid
        if day not in ['day1', 'day2', 'day3', 'day4']:
            return Response({"error": "Invalid day"}, status=status.HTTP_400_BAD_REQUEST)

        # Check If Day is active
        active_day = ActiveDay.objects.first()
        if day != active_day.day:
            return Response({"error": "Day is Not Active"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if already marked present
        if getattr(student, f'is_present_{day}'):
            return Response({"error": "Already marked present"}, status=status.HTTP_400_BAD_REQUEST)

        # Mark present and update timestamp
        setattr(student, f'is_present_{day}', True)
        setattr(student, f'timestamp_{day}', timezone.now())
        student.save()

        return Response({"msg": "Successfully Marked Present"}, status=status.HTTP_200_OK)

class PresentStudentsListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = StudentSerializer

    def get_queryset(self):
        day = self.kwargs.get('day')

        if day not in ['day1', 'day2', 'day3', 'day4']:
            return Student.objects.none()

        queryset = Student.objects.filter(**{f'is_present_{day}': True})
        queryset = queryset.order_by(f'timestamp_{day}')

        return queryset
    
class UnmarkPresentView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = MarkPresentSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        student_number=validated_data['student_number']
        day = validated_data['day']
        student = get_object_or_404(Student, student_number=student_number)

        # Check if student exists
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if day is valid
        if day not in ['day1', 'day2', 'day3', 'day4']:
            return Response({"error": "Invalid day"}, status=status.HTTP_400_BAD_REQUEST)

        # Check If Day is active
        active_day = ActiveDay.objects.first()
        if day != active_day.day:
            return Response({"error": "Day is Not Active"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        # Check if student is marked present
        if not getattr(student, f'is_present_{day}'):
            return Response({"error": "Student not marked present"}, status=status.HTTP_400_BAD_REQUEST)

        # Unmark present
        setattr(student, f'is_present_{day}', False)
        setattr(student, f'timestamp_{day}', None)
        student.save()

        return Response({"msg": "Successfully Unmarked Present"}, status=status.HTTP_200_OK)

class DetailsView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'student_number'
