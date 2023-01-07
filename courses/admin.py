from django.contrib import admin
from courses.models import Course, Teacher, CourseTeacher, CourseReview


class CourseAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')



class TeacherAdmin(admin.ModelAdmin):
    pass


class CourseTeacherAdmin(admin.ModelAdmin):
    pass


class CourseReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(CourseReview, CourseReviewAdmin)
admin.site.register(CourseTeacher, CourseTeacherAdmin)

# Register your models here.
