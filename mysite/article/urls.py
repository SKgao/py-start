# 引入path
from django.urls import path
# 引入views.py
from . import views

# app名称
app_name = 'article'

# url
urlpatterns = [
    # path将url映射到视图
    path('article_list/', views.article_list, name='article_list')
]
