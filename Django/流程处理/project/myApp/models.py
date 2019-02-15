from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Grades(models.Model):



    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table = "grades"
#自定义管理器类
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)

    def createStudent(self,name, age, gender, contend, grade):
        stu = self.model()
        print(type(stu))


class Students(models.Model):
    # 定义一个类方法创建对象
    @classmethod
    def createStdents(cls, name, age, gender, contend, grade):
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend, sgrade=grade)
        return stu
    #自定义模型管理器
    #当自定义模型管理器，objects就不存在了
    stuObj = models.Manager()
    stuObj2 = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey('Grades')
    def __str__(self):
        return self.sname
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "students"
        ordering = ['id']

