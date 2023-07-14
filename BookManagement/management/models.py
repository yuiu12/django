from django.db import models

# Create your models here.
class Book(models.Model):
    #verbose_name 为字段提供一个可读性良好的字段名称
    #CharField为字符类型的字段，存储字符串类型的数据，max_length该字段所需存储的字符串的长度
    name = models.CharField(max_length=128,verbose_name='书籍名称')
    author = models.CharField(max_length=64,verbose_name='作者')
    #default 为该字段设置默认值
    #FloatField浮点数类型的字段，存储一个实数，
    price = models.FloatField(default=0.0,verbose_name='定价')
    #blank设置为True，保存书籍这个字段的输入框可以留空
    #DateField日期字段，存储日期数据，
    publish_date = models.DateField(null=True,blank=True,verbose_name='出版日期')
    category = models.CharField(max_length=32,default='未分类',verbose_name='书籍分类')
    #无论是update还是.save()都不能更改他的值，一般用于记录数据的创建时间
    #DataTimeField日期时间字段，
    create_datetime = models.DateTimeField(auto_now_add=True,verbose_name='添加日期')
    def __str__(self): #定义str方法后，在将模型对象作为参数传递给str函数时将会调用该方法返回响应的字符串
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=128,verbose_name='图片名称')
    #textField 文本字段。存储大量文本，无需指定最大长度
    description  = models.TextField(default='',verbose_name='图片描述')
    #ImageField图片字段，回验证上传对象是否为图片
    img = models.ImageField(upload_to='image/%Y/%m/%d/',verbose_name='图片')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name='所属书籍')
    def __str__(self):
        return self.name
