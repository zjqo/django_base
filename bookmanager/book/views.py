from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
#视图，就是python函数
# 两个要求
# 	1、视图函数的第一个要求就是接受请求，就是httprequest
# 	2、必须返回一个响应
def index(requset):
    return HttpResponse('ok')