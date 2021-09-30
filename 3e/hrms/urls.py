from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/<int:pk>/', views.EmployeeDetailsView.as_view()),
    path('employeesfull/<int:pk>/', views.EmployeeFullDetailsView.as_view()),
    path('emp/', views.EmployeeList.as_view()),
    path('emp/<int:pk>/', views.EmployeeDetail.as_view()),
]