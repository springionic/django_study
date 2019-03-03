# Django系统
- 环境
    - python3.6
    - django1.8
- 参考资料
    - [django中文教程](http://python.usyiyi.cn)
    - django架构的16堂课
# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list：显示当前环境安装的包
    - conda env list：显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - (Linux) source activate env_name
        - (Window) activate env_name
    - pip install django=1.8
    
# 后台需要的流程

# 创建第一个Django程序
- 命令行启动

        django-admin startproject tulingxueyuan
        cd tulingxueyuan
        python manage.py runserver
- pycharm启动
    - 需要配置
    
# 路由系统-urls
- 创建app
    - app：负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher
- 路由
    - 按照具体请求的url，导入到相应的业务处理模块的一个功能
    - django的信息控制中枢
    - 本质上是接收的url和相应的处理模块的一个映射
    - 在接收url请求的匹配上使用了re
    - url的具体格式如urls.py中所示
- 需要关注两点
    - 接收的url是什么，即如何用re对传入url进行匹配
    - 已知url匹配到哪个处理模块
- url匹配规则
    - 从上往下一个一个对比
    - url格式是分级格式，则按照级别一级一级往下对比，主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url
        - 'one/two/three/'
    - 正则以r开头，表示不需要转义，注意尖号(^)和美元符号($)
        - 'one/two/three' 配对 r'^one/
        - 'oo/one/two/three' 不配对 r'^one/"
        - 'one/two/three/' 配对 r'three/$'
        - 'oo/one/two/three/oo/' 不配对  r'three/$"
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容，则报错

# 正常映射
- 把某一个符合re的url映射到事物处理函数中去
    - 举例如下
    
            '''
            from showeast import views as sv
            
            urlpatterns = [
                url(r'^admin/', admin.site.urls)
                url(r'^normalmap', sv.normalmap)
                ]
            '''
# url中带参数映射
- 在事件处理代码中需要由url传入参数，形如 /myurl/param 中的param
- 参数都是字符串形式，如果需要整数形式需要自行转换
- 通常的形式如下

        '''
        /search/page/432 中的432需要经常性变换，
        '''
        
# url在app中处理
- 如果把所有应用url都集中tulingxueyuan.urls.py中，可能导致文件的臃肿
- 可以把urls的具体功能逐渐分散到每个app中
    - 从django.conf.urls 导入include
    - 注意此时re部分的写法
    - 添加include导入
- 使用方法
    - 确保include是被导入的
    - 写主路由的开头url
    - 写子路由
    - 编写视图
- 同样可以使用参数

# url中的嵌套参数
- 捕获某个参数的一部分
- 例如url   /index/page-3，需要捕获数字3为参数

        url(r'index_1/(page-(\d+)/)?$', sv.myindex_1)   # 不太好
        url(r'index_2/(?:page-(?P<page_numble>\d+)/)?$', sv.myindex_2)
- 上面例子会得到两个参数，但 ?: 表明忽略此参数

# 传递额为参数
- 参数不仅仅来自以url，还可能是我们自己定义的内容

        url(r'extrem/$', sv.extremParam, {'name': 'liuying'})
        
    - 附加参数同样适用于include语句，此时对include内所有都添加
    
# url的反向解析
- 防止硬编码
- 本质上是对每一个url进行命名
- 以后再编码代码中使用url的值，原则上都应该使用反向解析


# views 视图
## 1.视图概述
- 视图即视图函数，接收web请求并返回web响应的事物处理函数
- 响应指符合http协议要求的任何内容，包括json，string，html等
- 本章忽略事物处理，重点在如何返回处理结果上
## 2.其它简单视图
- django.http给我们提供的类很多和HttpResponse类似的简单视图，通过查看django.http源码我们可以看到啊
- 此类视图使用方法基本相似，可以通过return语句直接反馈给浏览器
- Http404为Exception子类，所以需要raise使用
## 3.HttpResponse详解
- 方法
    - init：使用页面内容实例化HttpResponse对象
    - write(content)：以文件的方式写
    - flush(): 以文件的方式输出缓冲区
    - set_cookie(key, value='', max_age=None, expires=None): 设置cookie
        - key,value都是字符串类型
        - max_age是一个整数，表示在指定秒数后过期
        - expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期
        - max_age与expires二选一
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key): 删除指定的key的cookie，如果key不存在则什么也不发生

    
   