from django.http import JsonResponse
from django.shortcuts import render

from cbo.models import Blog, UserManagerObject
from django.contrib import auth
from django.contrib.auth.models import User
from cbo.models import UserManager
from cbo.models import User

# Create your views here.
# 获取博客推荐列表
def blogrecom_req(request):
    # params 有两个参数，一个是num，一个是keyword
    num = int(request.GET.get('num'))
    keyword = request.GET.get('keyword')

    # 从blog表中随机获取min(num, len(blog))个数据
    blog = Blog.objects.all()
    # blog = blog.filter(blog_recommand=1)
    blog = blog.filter(blog_title__contains=keyword)
    blog = blog.order_by('?')
    blog = blog[:min(num, len(blog))]

    # 将数据转换成json格式
    lst = []
    for var in blog:
        # make var to dict
        var1 = vars(var)
        var1.pop('_state')
        lst.append(var1)
        print(var1)

    # 返回json数据
    return JsonResponse({
        'context': lst,
        'success': "sucess",
        'echo_str': ''
    }, safe=False)


def rigister(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('passwd')
        email = request.POST.get('email')

        # 判断用户名是否已经存在
        is_exists = User.objects.filter(username=username).first()
        # print(is_exists)
        if is_exists != None:
            return JsonResponse({
                'context': '',
                'success': "fail",
                'echo_str': '用户名已存在'
            }, safe=False)
        else:
            User.objects.create_user(username=username, password=password, email=email)
            return JsonResponse({
                'context': '',
                'success': "sucess",
                'echo_str': '注册成功'
            }, safe=False)
