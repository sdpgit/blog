"""定义blogs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示单条blog内容页面
    url(r'^blogpost/(?P<blogpost_id>\d+)/$', views.blogpost, name='blogpost'),

    # 添加blog页面
    url(r'^new_blog$', views.new_blog, name='new_blog'),

    # 修改blog页面
    url(r'^edit_blog/(?P<blogpost_id>\d+)/$', views.edit_blog,
        name='edit_blog'),
]
