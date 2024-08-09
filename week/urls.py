from django.urls import path,include
from .import views

urlpatterns = [
    # path('index', views.index),
    # path('jan',views.jan)
    path('<int:week>',views.week_details_number),
    path('<str:week>',views.week_details,name="week-details"),
    path('<str:week>',views.week_details,name="week"),
    path('<str:week>',views.week_details,name="details"),
    
]
