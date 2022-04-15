from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('lawapp.urls'))
    path('register', views.register, name='register'),
    # path('login', views.register, name='register')
   
]
