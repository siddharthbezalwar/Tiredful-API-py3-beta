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

    # ex: /exams/
    path('', views.index, name='index'),

    # ex: /exams/score_card>
    path('exams/<str:score_card>/', views.get_score, name='exams'),
]
