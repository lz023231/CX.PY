from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
def index(request):
    #return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')

from .models import Students,Grades
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request,'myApp/students.html',{"students":studentsList})


#分页显示学生
def stupage(request,page):
    page = int(page)
    studentsList = Students.stuObj2.all()[(page-1)*5:page * 5]
    return render(request, 'myApp/students.html', {"students": studentsList})



def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStdents("刘德华",34,True,"woidf",grade)
    stu.save()
    return HttpResponse('sdfsd')