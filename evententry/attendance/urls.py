from django.urls import path
from .views import MarkPresentView, PresentStudentsListView, UnmarkPresentView, DetailsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("generate/", TokenObtainPairView.as_view()),
    path('mark_present/<str:student_number>/<str:day>/', MarkPresentView.as_view(), name='mark_present'),
    path('present_students/<str:day>/', PresentStudentsListView.as_view(), name='present_students'),
    path('unmark_present/<str:student_number>/<str:day>/', UnmarkPresentView.as_view(), name='unmark_present'),
    path('details/<str:student_number>/', DetailsView.as_view(), name='student_details'),
]
