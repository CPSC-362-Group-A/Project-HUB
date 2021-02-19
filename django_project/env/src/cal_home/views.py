
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'cal_home/home.html')


def main(request):
    return render(request, 'cal_home/main.html')
def about(request):
    return render(request, 'cal_home/about.html')