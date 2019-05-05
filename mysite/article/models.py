from django.db import models

# 导入内建User模型
from django.contrib.auth.models import User
# timezone用于处理时间事务
from django.utils import timezone

# blog文章数据模型
class ArticlePost(models.Model):

    # 参数 on_delete 用于指定数据删除的方式，避免两个关联表的数据不一致。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # models.CharField 为字符串字段，用于保存较短的字符串
    title = models.CharField(max_length=100)

    # models.CharField 保存大量文本使用
    body = models.TextField()

    # 参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类 Meta用来使用类提供的模型元数据
    class Mate:
        # ordering定义了数据的排列方式
        # -created表示将以创建时间的倒序排列
        ordering = ('-created', )

    def __str__(self):
        return self.title