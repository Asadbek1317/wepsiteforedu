from django import forms
from courses.models import CourseReview


class CourseReviewForm(forms.ModelForm):
    stars_given = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = CourseReview
        fields = ('stars_given', 'comment')
