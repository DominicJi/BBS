from django.conf.urls import url
from app01 import views
urlpatterns=[
    url(r'(.*)/article/(\d+)/$',views.article_detail),
    url(r'(.*)/(category|tag|archive)/(.*)/$',views.index),
    url(r'(.*)/',views.index)
]