from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    phone=models.CharField(max_length=11)
    avatar=models.FileField(upload_to='media/avatar/',default='media/avatar/default.png')

    blog=models.OneToOneField(to='Blog',to_field='nid',null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

class Blog(models.Model):
    nid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=64)
    theme=models.CharField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name

class Category(models.Model):
    nid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    blog=models.ForeignKey(to='Blog',to_field='nid')

    def __str__(self):
        return '{}-{}'.format(self.blog.title,self.title)

    class Meta:
        verbose_name='文章分类'
        verbose_name_plural=verbose_name

class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)  # 标签名
    blog = models.ForeignKey(to="Blog", to_field="nid")  # 所属博客

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)  # 文章标题
    desc = models.CharField(max_length=255)  # 文章描述
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    category = models.ForeignKey(to="Category", to_field="nid", null=True)

    user = models.ForeignKey(to="UserInfo", to_field="nid")

    #评论数
    comment_count=models.IntegerField(default=0)
    #点赞数
    up_count=models.IntegerField(default=0)
    #反对数
    down_count=models.IntegerField(default=0)

    tags = models.ManyToManyField(
        to="Tag",
        through="Article2Tag",
        through_fields=("article", "tag"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

class ArticleDetail(models.Model):
    """
    文章详情表
    """
    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.OneToOneField(to="Article", to_field="nid")

    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name


class Article2Tag(models.Model):
    """
    文章和标签的多对多关系表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid")
    tag = models.ForeignKey(to="Tag", to_field="nid")

    def __str__(self):
        return "{}-{}".format(self.article, self.tag)

    class Meta:
        unique_together = (("article", "tag"),)
        verbose_name = "文章-标签"
        verbose_name_plural = verbose_name


class ArticleUpDown(models.Model):
    """
    点赞表
    """
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="UserInfo", null=True)
    article = models.ForeignKey(to="Article", null=True)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = (("article", "user"),)
        verbose_name = "点赞"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """
    评论表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid")
    user = models.ForeignKey(to="UserInfo", to_field="nid")
    content = models.CharField(max_length=255)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name


# class article(models.Model):
#     title=models.CharField(max_length=32)
#     publisher_date=models.DateField()
#     info=models.CharField(max_length=64)
#     detail=models.OneToOneField(to='Article_detail')
#     author=models.ForeignKey(to=Userinfo)
#     Category=models.ForeignKey(to=Category)
#
# class Article_detail(models.Model):
#     content=models.CharField(max_length=-1)
#
#
# class Blog(models.Model):
#     Theme=models.CharField(max_length=32)
#     title=models.CharField(max_length=32)
#     user=models.OneToOneField(to=Userinfo)
#
# class Category(models.Model):
#     cname=models.CharField(max_length=32)
#
# class Comment(models.Model):
#     content=models.CharField(max_length=64)
#     user=models.ForeignKey(to=Userinfo)
#     double_id=models.ForeignKey('self')
#
#
# class Poll(models.Model):
#      pass
