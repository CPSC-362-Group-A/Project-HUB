
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return render(request, 'cal_home/landing.html')
def test(request):
    return render(request, 'cal_home/test.html')
def calendar(request):
    return render(request, 'cal_home/calendar.html')
def about(request):
    return render(request, 'cal_home/about.html')