
from django.urls import path,include
from .import views

urlpatterns = [
    # path('index', views.index),
    # path('jan',views.jan)
    path('<int:month>',views.month_details_by_number),
    path('<str:month>',views.month_details,name="month-details"),
    path('<str:month>',views.month_details,name="month"),
    path('<str:month>',views.month_details,name="details"),
    
]