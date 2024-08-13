from django.urls import path,include
from .import views
urlpatterns = [
    path('auth',views.index,name='author-name'),
    
]

