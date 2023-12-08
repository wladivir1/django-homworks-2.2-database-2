from django.contrib import admin

from .models import Student, Teacher


class TeacherInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 2    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = ['group']
    inlines = [TeacherInline,]
    




@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
