from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),

    url(r'^students/$', views.students),
    url(r'^stu/(\d+)/$', views.stupage),
    url(r'^addstudent/$', views.addstudent)
]