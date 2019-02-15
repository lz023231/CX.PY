流程梳理：1、创建工程-------执行<django.admin startproject project>
		 2、创建项目-------执行<python manage.py startapp myApp>
		 3、激活项目-------修改<settings.py中的INSTALLED_APPS>
		 4、配置数据库-----1、修改__init__.py文件
		 				 2、修改settings.py文件中的DATABASE
		 5、创建模型类-----在项目目录下的models.py文件中
		 6、生成迁移文件---执行<python manage.py makemigrations>
		 7、执行迁移------执行<python manage.py migrate>