from django.urls import path
from base import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('create',views.create, name='create'),
    path('read/<int:pk>',views.read,name='read'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('event',views.event,name='event'),
    path('news',views.news,name='news'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('about',views.about,name='about'),
]