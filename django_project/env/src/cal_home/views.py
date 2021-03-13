
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return render(request, 'cal_home/landing.html')
def test(request):
    return render(request, 'cal_home/test.html')