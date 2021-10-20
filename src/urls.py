"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from django.conf.urls import url

from myapp import views
from helloapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

# ---------------------------------CRUD OPERATIONS ----------------------------------
    path('student/', views.studentData, name="student_data"),                # myapp.view.py : Access the Home Page
    path('addStudentForm/', views.student_add_form),    # myapp.view.py : Access the Home Page
    path('addStudent/', views.student_add, name="student_add"),    # myapp.view.py : Access the Home Page
    path('editStudent/<sid>', views.student_edit, name="student_edit"),    # myapp.view.py : Access the Home Page
    path('delStudent/<sid>', views.student_del, name="student_del"),    # myapp.view.py : Access the Home Page

    # FORM Class
    path('addForm/', views.addForm),            # myapp.view.py : Access the Home Page

    path('search-form/', views.search_form),            # myapp.view.py : Access the Home Page
    path('search/', views.search),                # myapp.view.py : Access the Home Page

# -----------------------------------------------------------------------------------
    # path('', views.theme),                    # myapp.view.py : Access the Home Page
    path('', views.index),                      # myapp.view.py : Access the Home Page
    path('about/', views.about),                # myapp.view.py : Access the Home Page
    path('services/', views.services),          # myapp.view.py : Access the Home Page
    path('portfolio/', views.portfolio),        # myapp.view.py : Access the Home Page
    path('contact/', views.contact, name="cno"),            # myapp.view.py : Access the Home Page

# -----------------------------------------------------------------------------------
    path('home/', views.home),              # myapp.view.py : Access the Home Page
    path('show/', views.show),              # myapp.view.py : Displays Simple Message
    path('today/', views.displayDate),      # myapp.view.py : Displays current date
    
    path('hello/', hello),                 # helloapp.view.py : Access the Home Page
    path('abc/', abc),                     # helloapp.view.py : Simple Text Message
    path('crudops/', crudops),             # helloapp.view.py : Access the Home Page

    # url(r'', show)   
]
