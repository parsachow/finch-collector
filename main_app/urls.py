from django.urls import path
from . import views

urlpatterns = [
    # we define route using the path() function
    # in django, path is ALWAYS defined with a trailing slash 
    #the name doesn't have to match the views 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #make html templates files with the proper route and name
    path('finches/', views.finch_index, name='index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='detail'),
    #get_absolute_url from this path
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'), #pk is primary key which is just another name for id
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    #feeding URL
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    #toy and finch association URL
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    #toy URLs
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
