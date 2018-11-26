from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('extract/', views.extract, name='extract'),
    path('result/', views.result, name='result'),
    path('result/<int:pk>', views.result_detail, name='result_detail'),
    path('example/', views.example, name='example'),
    path('loading/', views.loading, name='loading'),
]