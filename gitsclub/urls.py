from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('#about',views.about, name='about'),
    path('new/', views.newmember, name='newmember'),
    path('groups/', views.groups, name='groups'),
    path('group/<int:id>', views.group, name='group'),
]
