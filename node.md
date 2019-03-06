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
## 4. HttpResponseRedirect
- 重定向，服务器端跳转
- 构造函数的第一个参数用来指定重定向的地址
- 案例 ShowViews/views.py
        
        # 在 east/urls 中添加一个内容
        url(r'^v10_1/', views.v10_1),
        url(r'^v10_2/', views.v10_2),
        url(r'^v11/', views.v11, name='v11'),
        
        # /east/ShowViews/views中添加内容
        def v10_1(request):
            return HttpResponseRedirect('/v11')
        def v10_2(request):
            return HttpResponseRedirect(reverse('v11'))
        def v11(request):
            return HttpResponse('哈哈哈，这是v11的访问返回！')
## 5.Request对象
- Request介绍
    - 服务器接收到http协议的请求后，会根据报文创建HTTPRequest对象
    - 视图函数的第一个参数是HTTPRequest对象
    - 在django.http模块中定义了HTTPRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path：一个字符串，表示请求的页面的完整路径，不包含域名
    - method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET', 'POST'
    - encoding：一个字符串，表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置，一般为utf-8
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码
    - GET：一个类似于字典的对象，包含get请求方式的所有参数
    - POST：一个类似于字典的对象，包含post请求方式的所有参数  
    - FILES：一个类似于字典的对象，包含所有的上传文件
    - COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符创
    - session：一个既可读又可写的类似于字典的对象，表示当前的会话
        - 只有当Django启用会话支持时才可用
        - 详细内容见‘状态保持’
    - 方法
        - is_ajax(): 如果请求是通过XMLHttpRequest发起的，则返回True
    - QueryDict对象
        - 定义在django.http.QueryDict
        - request对象的属性GET, POST都是QueryDict类型的对象
        - 与python字典不同，QueryDict类型的对像用来处理一个键带有多个值的情况
        - 方法get(): 根据键获取值
            - 只能获取键的一个值
            - 如果一个键同时拥有多个值，获取最后一个值
        - 方法getlist(): 根据键获取值
            - 将键的值以列表返回，可以获取一个键的多个值
    - GET属性
        - QueryDict类型的对象
        - 包含get请求的所有参数
        - 与url请求地址中的参数对应，位于 ? 后面
        - 参数的格式是键值对，如 key1=value1
        - 多个参数之间，使用 & 连接， 如 key1=value1&key2=value2
        - 键是开发人员定下来的，值是可变的
        - 案例 /views/v8_get
    - POST属性
        - QueryDict类型的对象
        - 包含post请求的所有参数
        - 与form表单中的控件对应
        - 表单中控件必须有name属性，name为键，value为值
            - checkbox存在一键多值的问题
        - 键是开发人员定下来的，值是可变的
        - 案例 /views/v9_post
            - settings中设置模板位置(已经设置完毕)
            - 设置get页面的urls和参数
        - 添加文件templates/for_post.html
        - 由于安全原因，需要在设置中安全选项中注释掉csrf设置
        - 还有对模板的添加设置
- 手动编写视图
    - 实验目的：
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理
    - 分析：
        - django把所有请求信息封装于request
        - django通过urls模块把相应请求跟事件处理函数链接起来，并把request作为参数传入
        - 在相应的处理函数中，我们需要完成两部分   
            - 处理业务
            - 把结果封装并返回，我们可以使用简单HttPResponse，同样也
        - 本案例不介绍业务处理，把目光集中在如何渲染结果并返回
    - render(request, template_name[,context][,context_instance][,content_type])
        - 使用模板和一个给定的上下文环境，返回一个渲染后的HttpResponse对象
        - request：django的传入请求
        - template_name：模板名称
        - content_instance：上下文环境
        - 案例参看代码 teacher_app/views/render_test 和 render2_test,render3_test
    - render_to_response
        - 根据给定的上下文字典渲染给定模板，返回渲染后的HttpResponse
        - 案例 render4_test
- 系统内建视图
    - 系统内建视图，可以直接使用
    - 案例 get404
        - default.page_not_found(request, template_name='404.html')
        - 系统引发Http404时触发
        - 默认传request_path变量给模板，即导致错误的url
        - debug = True则不会调用404，取而代之的是调试信息
        - 404视图会被传递一个RequestContext对象并且可以访问模本上下文处理器提供的变量
    - 500,403，400等不列举了
## 基于类的视图
- 难度和常用度问题
- 略                    
                    
   