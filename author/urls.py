from django.urls import path,include
from .import views
urlpatterns = [
    path('auth',views.index,name='author-name'),
    path('authors/auth-details/<int:Author>/',views.author_details,name='author-details'),
    
]

