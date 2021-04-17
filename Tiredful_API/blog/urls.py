# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# This file is part of Tiredful API application

from django.urls import path
from . import views

urlpatterns = [

    # ex: /blog/
    path('', views.index, name='index'),

    # ex: /articles/<article-id>
    path('articles/<int:article_id>/', views.article, name='articles'),

    # ex: /approve-article/<article_id>
    path('approve-article/<int:article_id>/', views.approve_article, name='approve-article'),

]
