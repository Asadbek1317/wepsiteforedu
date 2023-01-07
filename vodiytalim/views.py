from django.shortcuts import render

from courses.models import CourseReview


def landing(request):
    return render(request, "landing.html")


def home_page(request):
    course_reviews = CourseReview.objects.all().order_by('-created_at')

    return render(request, 'home.html', {'course_reviews': course_reviews})