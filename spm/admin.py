from django.contrib import admin
from .models import School_T, Department_T, Program_T, Student_T, Course_T, Pre_req_course_T, PLO_T, CO_T, Faculty_T, VC_T, GFaculty_T, Department_Head_T, Dean_T
# Register your models here.
admin.site.register(School_T)
admin.site.register(Department_T)
admin.site.register(Program_T)
admin.site.register(Student_T)
admin.site.register(Course_T)
admin.site.register(Pre_req_course_T)
admin.site.register(PLO_T)
admin.site.register(CO_T)
admin.site.register(Faculty_T)
admin.site.register(VC_T)
admin.site.register(Dean_T)
admin.site.register(Department_Head_T)
admin.site.register(GFaculty_T)
