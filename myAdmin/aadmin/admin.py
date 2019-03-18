from django.contrib import admin
from aadmin.models import Student, ClassRoom, Teacher

# Register your models here.
admin.site.site_header = '这是站头'
admin.site.site_title = '这是站标题'
admin.site.index_title = '这是首页标语'

class ClassRoomAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ['name', 'room', 'curTime', 'getRoomName']
    search_fields = ['name']
    fieldsets = (
        ('基本信息', {'fields': ['name']}),
        ('其它信息', {'fields': ['course', 'room']})
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
# admin.site.register(Teacher, TeacherAdmin)


