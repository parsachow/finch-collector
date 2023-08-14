from django.urls import path
from . import views

urlpatterns = [
    # we define route using the path() function
    # in django, path is ALWAYS defined with a trailing slash 
    #the name doesn't have to match the views 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_index, name='index')
]
