from django.urls import path
from .views import *
urlpatterns = [path('creat',creat_view.as_view(), name = 'creat'),
               path('lis',list_view.as_view(),name = 'lis_view'),
               path('update/<pk>',update_view.as_view(),name = 'update_view'),
               path('del/<pk>',del_view.as_view(),name = 'del_view'),]

