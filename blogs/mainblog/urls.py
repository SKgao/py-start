
from django.urls import path, include

import mainblog.views

urlpatterns = [
    path('hello_world', mainblog.views.hello_world),
    path('content', mainblog.views.article_content)
]