# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# This file is part of Tiredful API application

"""Tiredful_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    
    # URL for user login
	path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # URL for including intro app.
    path('', include(('intro.urls', 'intro'), namespace="intro")),

    # URL for including library app
    path('api/v1/', include(('library.urls', 'library'), namespace="library-api")),
    path('library/', include(('library.urls', 'library'), namespace="library")),

     # URL for including exams app
    path('api/v1/', include(('exams.urls', 'exams'), namespace="exams-api")),
    path('exams/', include(('exams.urls', 'exams'), namespace="exams")),

     # URL for including blog app
    path('api/v1/', include(('blog.urls', 'blog'), namespace="blog-api")),
    path('blog/', include(('blog.urls', 'blog'), namespace="blog")),

    # URL for including trains app
    path('api/v1/', include(('trains.urls', 'trains'), namespace="trains-api")),
    path('trains/', include(('trains.urls', 'trains'), namespace="trains")),

    # URL for including health app
    path('api/v1/', include(('health.urls', 'health'), namespace="health-api")),
    path('health/', include(('health.urls', 'health'), namespace="health")),

    # URL for including advertisements app
    path('api/v1/', include(('advertisements.urls', 'advertisements'), namespace="advertisements-api")),
    path('advertisements/', include(('advertisements.urls', 'advertisements'), namespace="advertisements")),

     # URL for including broken-token app
    path('api/v1/', include(('broken_token.urls', 'broken_token'), namespace="broken-token-api")),
    path('jwt-token/', include(('broken_token.urls', 'broken_token'), namespace="broken-token")),

]
