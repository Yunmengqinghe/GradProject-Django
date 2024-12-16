"""
URL configuration for GPMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
import College.views

urlpatterns = [
    path('', College.views.login),
    path('admin/', admin.site.urls),
    path('college/', include(('College.urls', 'college'), namespace = 'college')),
    path('mentor/', include(('Mentor.urls', 'mentor'), namespace = 'mentor')),
    path('student/', include(('Student.urls', 'student'), namespace = 'student')),
    path('collegeadmin/', include(('CollegeAdmin.urls', 'collegeadmin'), namespace = 'collegeadmin')),

]
