from django.urls import path

from . import views

urlpatterns = [
    path('', views.collect_user_info, name='index'),

]
