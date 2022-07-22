from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.loginUser,name='login'),
    path('signup/',views.signupUser,name='signup'),
    path('add/',views.add_todo,name='add'),
    path('logout/',views.logoutUser,name='logout'),
    path('delete/<int:id>',views.delete_todo,name='delete/<int:id>'),
    path('change-status/<int:id>/<str:status>',views.change_todo,name='change-status/<int:id>/<str:status>'),
]