from django.contrib import admin

# Register your models here.
from .models import Grades,Student

#注册
class StudentInfo(admin.TabularInline):
    model = Student
    extra = 2
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]
    #列表属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']    #过滤器
    search_fields = ['gname']
    list_per_page = 5   #分页


    #添加、修改页属性
    #fields = []    #规定属性的先后顺序
    '''
    fieldsets = [
        ("num",{"fields":['ggirlnum','gboynum']}),
        ()
     ]  给属性分组
    '''

admin.site.register(Grades, GradesAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = "性别"
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
    list_per_page = 10
    #执行动作位置
    actions_on_top = True



#admin.site.register(Student,StudentAdmin)