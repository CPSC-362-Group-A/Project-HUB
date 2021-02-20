from django.urls import path
from cal_home import views

urlpatterns = [
    path('', views.landing, name ='cal_landing'),
    
    path('test/', views.test, name ='cal_test'),
    path('calendar/', views.calendar, name ='cal_calendar'),
    path('about/', views.about, name ='cal_about'),
]
