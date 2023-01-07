from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from courses.forms import CourseReviewForm
from courses.models import Course, CourseReview


# Create your views here.

class CourseView(View):
    def get(self, request):
        courses = Course.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            courses = courses.filter(title__icontains=search_query)

        return render(
            request,
            'courses/list.html',
            {'courses': courses, 'search_query': search_query}
        )


class CourseDetailView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        review_form = CourseReviewForm()

        return render(request, 'courses/detail.html', {"course": course, 'review_form': review_form})


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        course = Course.objects.get(id=id)
        review_form = CourseReviewForm(data=request.POST)

        if review_form.is_valid():
            CourseReview.objects.create(
                course=course,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse("courses:detail", kwargs={'id': course.id}))

        return render(request, "courses/detail.html", {"course": course, 'review_form': review_form})


