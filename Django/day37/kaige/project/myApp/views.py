from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
def index(request):
    #return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')



def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")


#获取get传递的数据
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + "  " + b + "  " + c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1+ "  " + a2 +"  " + c)




#post
def showregist(request):
    return render(request,'myApp/regist.html')
def regist(request):
    pass








































