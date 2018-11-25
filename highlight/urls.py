from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('extract/', views.extract, name='extract'),
    path('result/', views.result, name='result'),
    #example에서 result페이지로 넘어갈때 페이지 인자
    path('result/<int:music_id>', views.result, name='result'),
    path('example/', views.example, name='example'),
    path('loading/', views.loading, name='loading'),
]