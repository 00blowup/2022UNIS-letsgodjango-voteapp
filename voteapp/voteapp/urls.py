"""voteapp URL Configuration

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
from django.urls import path
from votes import views

urlpatterns = [
    path('', views.view_all_polls),

    path('polls/', views.view_all_polls, name='view_all_polls'),
    path('polls/create/', views.create_poll, name='create_poll'),
    path('polls/<int:id>/', views.view_poll_by_id, name='view_poll_by_id'),
    path('polls/<int:id>/vote', views.vote_poll, name='vote_poll'),
    path('polls/<int:id>/update/', views.update_poll, name='update_poll'),
    path('polls/<int:id>/delete/', views.delete_poll, name='delete_poll')
]
