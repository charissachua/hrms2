"""3e URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
#    path('users', views.Users.as_view(), name='users'),
#     path('create/', views.UserCreateView.as_view(), name='create_user'),
#     path('update/<int:pk>', views.UserUpdateView.as_view(), name='update_user'),
#     path('delete/<int:pk>', views.UserDeleteView.as_view(), name='delete_user'),
#     path('change/<int:pk>', views.ChangePasswordView.as_view(), name='change_password'),

#    path('employees/', views.EmployeeList.as_view()),


    #    path('employees', views.getAllStaff, name='employees'),
#    path('departments', views.getAllDepartments),
#    path('profile/<int:pk>', views.getStaffDetails, name='profile'),

    path('admin/', admin.site.urls),
    path('hrms/', include('hrms.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
