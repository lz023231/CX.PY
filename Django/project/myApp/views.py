from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("sunck is a good man!")
def detail(request,num):
    return HttpResponse("detail-%s"% num)

from .models import Grades
def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板,模板在渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades..html',{"grades":gradesList})


from .models import Student
def student(request):
    studentList = Student.objects.all()
    return  render(request,'myApp/student.html',{"student":studentList})