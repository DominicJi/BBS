from django import template
from app01 import models

register = template.Library()


@register.inclusion_tag('left_tag.html')
def left_panel(username):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    blog = user_obj.blog
    from django.db.models import Count
    category_list = models.Category.objects.filter(blog=blog).annotate(num=Count('article')).values('title', 'num')
    tag_list = models.Tag.objects.filter(blog=blog)
    data_list = models.Article.objects.filter(user=user_obj).extra(
        select={'date': "DATE_FORMAT(create_time,'%%Y-%%m')"}).values('date').annotate(num=Count('nid')).values('date',
                                                                                                                'num')
    return {'username':username,'category_list':category_list,'data_list':data_list,'tag_list':tag_list}