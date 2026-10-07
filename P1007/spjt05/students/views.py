from django.shortcuts import render



# Create your views here.
#학생성적 입력
def swrite(request) :
    return render(request,'swrite.html')


def slist(request) :
    return render(request,'slist.html')