from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('re', views.read_view, name='re'),
    path('update/<int:id>', views.update, name='update'),
]
