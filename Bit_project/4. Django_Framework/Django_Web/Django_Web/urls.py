"""Django_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from account.views import index, logout, RegisterView, LoginView, signup_complete
from content.views import content, contact, contact_complete
from modelpage.views import sample, photo
from board.views import board_list, board_write, board_detail
from graph.views import Realtimegraph
from map.views import Realtimemap
from Imageanalysis.views import Imageanalysis, Imageanalysis_detail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('index/', index),
    path('logout/', logout),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('signup_complete/', signup_complete),

    path('content/', content),
    path('contact/', contact),
    path('contact_complete/', contact_complete),
    path('sample/', sample),
    path('photo/', photo, name='img'),

    path('Imageanalysis/', Imageanalysis),
    path('Imageanalysis_detail/', Imageanalysis_detail, name='img2'),

    path('board_list/', board_list),
    path('board_detail/<int:pk>/', board_detail),
    path('board_write/', board_write),

    path('Realtimegraph/', Realtimegraph),
    path('Realtimemap/', Realtimemap),
]
