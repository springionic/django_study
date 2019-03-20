# Django REST Framework
## 1. REST
- 前后端分离
- API  ApplicationProgrammingInterface
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