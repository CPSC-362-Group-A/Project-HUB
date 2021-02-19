
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #empty path maches with the empty url in the cal_home to make the homepage
    path('', include('cal_home.urls')),
]
