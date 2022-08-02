from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('ok')



##############新增数据##################
from book.models import bookinfo
book = bookinfo(
    name='django',
    pub_date='2001-1-2',
    readcount=10
)
#必须调用book.save()才能保存到数据库

####################新增数据2##################################

#objects -- 相当于一个代理，实现曾删改查
bookinfo.objects.create(
    name = 'linux',
    pub_date= '2022-1-1',
    readcount = 20
)
##################修改数据###################################
book=bookinfo.objects.get(id=4)
book.name='ubuntu'
#必须调用book.save()才能保存到数据库

##################修改数据2###################################
#filter 过滤
bookinfo.objects.filter(id=4).update(name='centeros',commentcount=66)


#######################删除数据#####################################
# 删除分为两种删除一种为物理删除（将这条记录和数据删除）另一种为逻辑删除（修改标记位 列：is_delete = False)
book = bookinfo.objects.get(id = 4)
book.delete()

#############################删除数据2##################################
bookinfo.objects.get(id = 4).delete()
bookinfo.objects.filter(id=4).delete()

#################### 查询#################################
try:
    book=bookinfo.objects.get(id=1)
except bookinfo.DoesNotExist:
    print('not in')
book

books=bookinfo.objects.all()

bookinfo.objects.all().count()#获取数量


##########################过滤查询2#########################

#模型类名.objects.filter(属性名__运算符=直)，获取n个直，exclude()和get()一样的只是获取的直的个数不一样
book = bookinfo.objects.get(id__exact=1)#标准
book = bookinfo.objects.get(id=1)
bookinfo.objects.get(pk=1)

bookinfo.objects.filter(id=1)#filter得到的是列表（多个），get()只得到一个
bookinfo.objects.filter(name__contains='s')#查询书名中包含s的书
bookinfo.objects.filter(name__endswith='s')#查询以s结尾的书
bookinfo.objects.filter(name__isnull=True)#查询空名的书
bookinfo.objects.filter(id__in=[1,3,5])
#大于：gt；小于：lt；大于等于：gte；小于等于：lte
bookinfo.objects.filter(id__gt=3)
#exclude()查询不符合的结果
bookinfo.objects.exclude(id=1)
bookinfo.objects.filter(pub_date__year=1999)#查询1999年发行的图书
bookinfo.objects.filter(pub_date__gt='1999-1-1')#查询1999-1-1后发行的书