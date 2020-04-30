from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# App view.py

# App定义一个方法 index()，用来渲染页面
def index(request):
    return render(request, 'index.html')

def ymd_with_params(request, year, month, day):
    """
    日期视图函数
    :param request:
    :return:
    """
    result = str(year) + '/' + str(month) + "/" + str(day)
    return HttpResponse(result)

def ymd_with_params1(request,year, month, day):
    """
    日期视图函数(正则表达式)
    :param request:
    :param year:
    :param month:
    :param day:
    :return:
    """
    result = str(year) + '/' + str(month) + "/" + str(day)
    return HttpResponse(result)

def with_extra_params(request, extra_param):
    """
    带额外的参数
    :param request:
    :param extra_param:
    :return:
    """
    return HttpResponse('Welcome to attention ' + extra_param)