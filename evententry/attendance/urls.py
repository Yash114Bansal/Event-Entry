from django.urls import path
from .views import MarkPresentView, PresentStudentsListView, UnmarkPresentView, DetailsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('mark_present/', MarkPresentView.as_view(), name='mark_present'),
    path('present_students/<str:day>/', PresentStudentsListView.as_view(), name='present_students'),
    path('unmark_present/', UnmarkPresentView.as_view(), name='unmark_present'),
    path('details/<str:student_number>/', DetailsView.as_view(), name='student_details'),
]
