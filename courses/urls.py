from django.urls import path
from courses.views import CourseView, CourseDetailView, AddReviewView

app_name = 'courses'

urlpatterns = [
    path('', CourseView.as_view(), name='list'),
    path("<int:id>/", CourseDetailView.as_view(), name="detail"),
    path("<int:id>/reviews/", AddReviewView.as_view(), name='reviews'),
]