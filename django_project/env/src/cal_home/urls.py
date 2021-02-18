from django.urls import path
from cal_home import views

urlpatterns = [
    path('', views.home, name ='cal_home'),
    
    path('main/', views.main, name ='cal_main'),
    path('about/', views.about, name ='cal_about'),
]
