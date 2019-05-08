
from django.urls import path, include

import mainblog.views

urlpatterns = [
    path('hello_world', mainblog.views.hello_world),
    path('content', mainblog.views.article_content),
    path('index', mainblog.views.get_index_page),
    path('detail/<int:acticle_id>', mainblog.views.get_detail_page)
]