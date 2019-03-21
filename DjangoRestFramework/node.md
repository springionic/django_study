# Django REST Framework
## 1. REST
- 前后端分离
- API  ApplicationProgrammingInterface
    - 为了应付千变万化的前端需求
- REST：RepresentionStateTrans
    - 2000年，Fieding博士提出
    - RESTful：遵守REST规范的技术而设计的软件可以成为RESTful
- REST规范
    1. URL代表一个资源，一个资源应该是一个名词
    2. 动作有HTTP的methods方法
    3. URL应该包含版本信息，版本信息也可以放在HTTP协议中
    4. 过滤信息，使用URL的参数代表过滤
    5. 返回值：每一个返回码都具有特定含义
    6. 返回格式：推荐固定具体格式
- DjangoRestFramework
    - 相关网站自己找
    - 安装：pip install djangorestframework
    - 版本问题：version 3.7 是基于1.xx版本django，之后是2.xx的
    - django_filter 依赖 djangorestframework 3.7
- DRF的主要任务
- 案例tlxy_drf
    - django-admin startproject tlxy_drf
    - python manage.py startapp case01
    - 配置settings的app
    - 配置urls
    - 创建三个模型：Student，Teacher，ClassRoom