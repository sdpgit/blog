from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogpostForm

# Create your views here.


def index(request):
    """blogs主页"""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)


def blogpost(request, blogpost_id):
    """显示单个blogpost"""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    context = {'blogpost': blogpost}
    return render(request, 'blogs/blogpost.html', context)


@login_required
def new_blog(request):
    """添加新的blog"""
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = BlogpostForm()
    else:
        # POST提交的数据，对数据进行处理
        form = BlogpostForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog(request, blogpost_id):
    """编辑blog"""
    blogpost = BlogPost.objects.get(id=blogpost_id)

    # 判断是否是登陆用户发表的博文
    if blogpost.owner != request.user:
        # raise Http404
        return HttpResponseRedirect(reverse('blogs:blogpost',
                                            args=[blogpost.id]))
    if request.method != 'POST':
        # 初次请求，使用当前blog填充表单
        form = BlogpostForm(instance=blogpost)
    else:
        # POST提交的数据，对数据进行处理
        form = BlogpostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogpost',
                                                args=[blogpost.id]))

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
