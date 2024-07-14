from django.urls import path

from newApp import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('service',views.service,name='service'),
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard2', views.dashboard2, name='dashboard2'),
    path('students', views.students, name='students'),
    path('student_list',views.student_list, name='student_list'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete,name='delete')
]