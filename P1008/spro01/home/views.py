from django.shortcuts import render

# Create your views here.

#메인페이지열기 - templates > index.html
def index(request) :
    return render(request, 'index.html')