# urls.py(App)
from django.urls import path, re_path

# 导入视图函数
# 视图函数：处理请求并返回响应信息
from . import views

urlpatterns = [
    # 指向视图函数index
    path('', views.index, name='index'),

    # 指向日期视图函数
    # year:字符串
    # month：整形
    # day：slug类型
    path('<year>/<int:month>/<slug:day>', views.ymd_with_params, name='ymd_with_params'),

    # 路由正则表达式
    # 函数：re_path(路由地址,视图函数)
    # 路由地址：year、month、day为3个参数
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.ymd_with_params1),

    # 新建一个路由地址airpython
    # 指向视图函数with_extra_params
    # 并带有参数，参数通过字典定义
    path('airpython', views.with_extra_params, {'extra_param': 'AirPython'}),

]
