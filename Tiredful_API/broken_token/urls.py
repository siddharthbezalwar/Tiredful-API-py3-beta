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

    # ex: /jwt-token/
    path('', views.index, name='index'),

    # ex: /jwt-token/info-disclosure
    path('info-disclosure/', views.info_disclosure, name='info-disclosure'),

    # ex: /jwt-token/jwt-none/
    path('jwt-none/', views.jwt_none, name='jwt-none'),

    # ex: /jwt-token/jwt-signing-algo/
    path('jwt-signing-algo/', views.jwt_signing_algo, name='jwt-signing-algo'),

    # ex: /jwt-token/jwt-logout/
    path('jwt-logout/', views.jwt_logout, name='jwt-logout'),

    # ex: /crack-jwt/
    path('crack-jwt/', views.crack_jwt, name='crack-jwt'),

    # ex: /get-jwt-token-hs256/
    path('get-jwt-token-hs256/', views.get_jwt_token_HS256, name='get-jwt-token-hs256'),

    # ex: /get-jwt-token-rs256/
    path('get-jwt-token-rs256/', views.get_jwt_token_RS256, name='get-jwt-token-rs256'),

    # ex: /obtain-jwt-token-hs256/
    path('obtain-jwt-token-hs256/', views.obtain_jwt_token_HS256, name='obtain-jwt-token-hs256'),

    # ex: /obtain-jwt-token-rs256/
    path('obtain-jwt-token-rs256/', views.obtain_jwt_token_RS256, name='obtain-jwt-token-rs256'),

    # ex: /joker-plan/
    path('joker-plan/', views.joker_plan, name='joker-plan'),

    # ex: /joker-master-plan/
    path('joker-master-plan/', views.joker_master_plan, name='joker-master-plan'),

    # ex: /logout/
    path('logout/', views.broken_logout, name='logout'),

    # ex: /secure-logout/
    path('secure-logout/', views.secure_logout, name='secure-logout'),



]
