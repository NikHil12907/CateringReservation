from django.urls import path, include
import catering.views
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('catering/', include('catering.urls')),
   
        
    
]