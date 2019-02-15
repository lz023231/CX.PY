from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^attribles',views.attribles),
    url(r'^get1/$',views.get1),
    url(r'^get2/$',views.get2),

    url(r'^showregist/$',views.showregist),
    url(r'^regist/$',views.regist),
]