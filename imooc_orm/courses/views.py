from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import AddressInfo, Teacher, Course, Student, TeacherAssistant
from django.db.models import F, Q

# Create your views here.

class AddressAPI(View):
    """地址信息"""

    def get(self, request, address_id):  # 接收一个参数的id, 指modde中的pid属性对应的字段,即表中的pid_id
        if int(address_id) == 0:  # 为0时表示为查询省 , 省的pid_id为null
            address_data = AddressInfo.objects.filter(pid__isnull=True).values('id', 'address')
        else:  # 查询市或者区县
            address_data = AddressInfo.objects.filter(pid_id=int(address_id)).values('id', 'address')
        area_list = []  # 转成list后json序列化
        for a in address_data:
            area_list.append({'id': a['id'], 'address': a['address']})
        # 然后通过jsonResponse返回给请求方, 这里是list而不是dict, 所以safe需要传入False.
        return JsonResponse(area_list, content_type='application/json', safe=False)


class IndexView(View):
    def get(self, request):
        # # 查询、检索、过滤
        # teacher = Teacher.objects.all()
        # print(teacher)
        # teacher2 = Teacher.objects.get(nickname='Jack')  # get()只能返回一条结果，否则会报错
        # print(teacher2)
        # teacher3 = Teacher.objects.filter(fans__gte=500)
        # for t in teacher3:
        #     print(f'讲师姓名{t.nickname}--粉丝数{t.fans}')
        # teacher4 = Teacher.objects.filter(fans__in=[666, 1244])
        # print(teacher4)
        # teacher5 = Teacher.objects.filter(nickname__icontains='A')
        # print(teacher5)
        # # 结果切片、排序、链式查询
        # print(Teacher.objects.all()[1:])
        # teacher6 = Teacher.objects.all().order_by('-fans')
        # for t in teacher6:
        #     print(t.fans)
        # print(Teacher.objects.filter(fans__gte=500).order_by('nickname'))
        # # 查看执行的原生SQL
        # print(Teacher.objects.filter(fans__gte=500).order_by('nickname').query)
        # # SELECT courses_teacher`. nickname`, `courses_teacher`. introduction`, `courses_teacher`.
        # # `fans`, `courses_teacher`. create_at`, `courses_teacher`. updated_at`
        # # FROM courses_teacher`WHERE courses_teacher`. fans` >= 500 ORDER  BY
        # # `courses_teacher`. `nickname`ASC

        # 返回新QuerySet API
        # 1. all(), filter(), order_by(), exclude(), reverse(), distinct()
        # print(Student.objects.all().exclude(nickname='A同学'))
        # 2. extra(), defer(), only() 实现字段别名，排除一些字段，选择一些字段
        # s3 = Student.objects.all().extra(select={'name': 'nickname'})
        # for s in s3:
        #     print(s.name)
        # 3. values(), value_list()  获取字典或者元组形式的QuerySet
        # print(Teacher.objects.values('nickname', 'fans'))
        # print(Teacher.objects.values_list('nickname', 'fans'))
        # 4. union(), intersection(), difference()  并集、交集、差集

        # 5. select_related() 一对一、多对一查询优化， prefetch_related()  一对一、一对多查询优化、反向查询
        # print(Teacher.objects.get(nickname='Jack').course_set.all())
        # 6. annotate（） 使用聚合计数、求和、平均数、 raw()  执行原生的SQL

        # # """不返回Query API"""
        # # 1.获取对象 get(), get_or_create(), first(), last(), latest(), earliest(), in_bulk()
        # print(Course.objects.first())
        # print(Course.objects.last())
        # # 2.创建对象 create(), bulk_create(), update_or_create() 创建，批量创建，创建或更新
        # # 3.更新对象 update(), update_or_create() 更新，更新或创建
        # Course.objects.filter(title='Java系列教程2').update(price=300)
        # # 4.删除对象 delete() 使用filter过滤
        # # 5.其它操作 exists(), count(), aggregate() 判断是否存在，统计个数，聚合

        """F与Q对象"""
        Course.objects.update(price=F('prince')-11)
        print(Course.objects.filter(volume__lte=F('price')*10))

        print(Course.objects.filter(Q(title__icontains='java') & Q(volume__lte==5000)))




        return render(request, 'address.html')