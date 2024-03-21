from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('add',views.home,name='home'),
    path('',views.list_view,name='list'),
    path('detail/<int:id>/', views.detail_view, name='detail_view'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    
    
    
    
    
]
