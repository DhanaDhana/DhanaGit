from django.contrib import admin
from testapp.models import Student,Course
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['age','sname','loc']
class CourseAdmin(admin.ModelAdmin):
    list_display=['cname','cfee']
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
