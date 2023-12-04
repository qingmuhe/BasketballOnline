from django.http import JsonResponse
from django.shortcuts import render

from cbo.models import Blog


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
