from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
#视图，就是python函数
# 两个要求
# 	1、视图函数的第一个要求就是接受请求，就是httprequest
# 	2、必须返回一个响应
def index(requset):
    # return HttpResponse('ok')
    context = {
        'name':'zjq'
    }
    #context 理解为将试图中的数据传递给模板 ,  html 采用{{变量}}形式来展示我们的数据
    return render(requset,'book/index.html',context=context)#绚烂模板