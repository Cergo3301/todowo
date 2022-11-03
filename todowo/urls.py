from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.currenttodos, name='currenttodos'),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #Todos
    path('create/', views.createtodo, name='createtodo'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>/', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/completed', views.completedtodo, name='completedtodo'),
    path('todo/<int:todo_pk>/delete', views.deletedtodo, name='deletedtodo'),
]
