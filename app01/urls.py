from django.conf.urls import url
from app01 import views
urlpatterns=[
    #添加评论信息
    url(r'add_comment/$',views.add_comment),
    url(r'(.*)/article/(\d+)/$',views.article_detail),
    url(r'(.*)/(category|tag|archive)/(.*)/$',views.index),
    url(r'(.*)/',views.index)
]