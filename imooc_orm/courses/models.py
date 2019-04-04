from django.db import models

# Create your models here.

# class Test(models.Model):   # 数据库中表名为: course_test
#     """
#     测试学习用
#     """
#     # 自增长字段
#     Auto = models.AutoField()
#     BigAuto = models.BigAutoField()
#
#     # 二进制数据
#     Binary = models.BinaryField()
#
#     # 布尔型
#     Boolean = models.BooleanField()
#     NullBoolean = models.NullBooleanField()
#
#     # 整型
#     PositiveSamllInteger = models.PositiveIntegerField(db_column='age')  # 5个字节
#     SmallInteger = models.SmallIntegerField(primary_key=False)  # 6个字节
#     PositiveInteger = models.PositiveIntegerField(verbose_name='我是这个字段的别名')  # 10个字节
#     Integer = models.IntegerField(unique=True)  # 11个字节
#     BigInteger = models.BigIntegerField(null=True, blank=True, db_index=True)  # 20个字节     Positive代表正数
#     # null表示在数据库里面是否能为空，blank表示前端提交来的是否能为空，db_index表示给这个字段建立索引
#
#     # 字符串类型
#     Char = models.CharField(max_length=100, help_text='这个是提示信息')  # varchar
#     Text = models.TextField(editable=False)  # longtext
#
#     # 时间日期类型
#     Date = models.DateField(unique_for_date=True, auto_now=True)  # 年月日
#     DateTime = models.DateTimeField(auto_now_add=True)  # 年月日时分秒
#     Duration = models.DurationField()  # int, Python timedelta 实现
#
#     # 浮点型
#     Float = models.FloatField()
#     Decimal = models.DecimalField(max_digits=4, decimal_places=2)  # 13.33  44.64
#
#     # 其它字段
#     Email = models.EmailField()  # 邮箱
#     Image = models.ImageField()  # 图片
#     File = models.FileField()  # 文件
#     FilePath = models.FilePathField()  # 文件路径
#     URL = models.URLField()  #
#     UUID = models.UUIDField()
#     GenericIPAdress = models.GenericIPAddressField()
#
#
# class A(models.Model):
#     onetoone = models.OneToOneField(Test, related_name='one')   # 一对一用这个
#
#
# class B(models.Model):
#     foreign = models.ForeignKey(A, on_delete=models.CASCADE)   # 一对多用这个
#
#
#
# class C(models.Model):
#     manytomany = models.ManyToManyField(B)  # 多对多用这个

# 字段的三大类型
#   1. 所有字段都有的参数
#   2. 个别字段具有的参数
#   3. 关系型字段的参数

# """
# on_delete 当一个被外键关联的对象被删除时，Django将模仿on_delete参数定义的SQL约束执行相应操作
# 如下6种操作
#     CASCADE：模拟SQL语言中的ON DELETE CASCADE约束，将定义有外键操作的模型对象同时删除！（为当前Django的默认操作）
#     PROTECT：阻止上面的删除操作，但是弹出ProtectedError异常
#     SET_NULL：将外键字段设为null，只有当字段设置了null=True时，可使用该值
#     SET_DEFAULT：将外键字段设为默认值，只有当前字段设置了default参数时，方可使用
#     DO_NOTHING：什么也不做
#     SET()：设置为一个传递给SET()的值或者一个回调函数的返回值，注意大小写
# """

class AddressInfo(models.Model):
    """省市县的地址信息"""
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='地址')
    pid = models.ForeignKey('self', null=True, blank=True, verbose_name='自关联')
    # pid = models.ForeignKey('AddressInfo', null=True, blank=True, verbose_name='自关联')

    def __str__(self):
        return self.address
