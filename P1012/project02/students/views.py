from django.shortcuts import render,redirect
from students.models import Students

# Create your views here.
#학생상세보기
def sview(request,name) :
    print(f'name 데이터 : {name}')
    qs = Students.objects.get(name=name)
    context ={'stu':qs}

    return render(request,'sview.html',context)
#학생정보수정
def supdate(request,name) :
    print(f'name 데이터 : {name}')
    qs = Students.objects.get(name=name)
    context ={'stu':qs}

    return render(request,'supdate.html',context)



def slist(request) :
    qs = Students.objects.all()

    context = {'list':qs}
    return render(request,'slist.html',context)


def swrite(request) :
    if request.method == 'GET':
        print('GET 출력')
        return render(request,'swrite.html')
    elif request.method == 'POST' :
        print('GET 출력')
        name = request.POST.get('name')
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')

        qs = Students(name=name,major=major,age=age,grade=grade,gender=gender)
        qs.save()
        return redirect('/students/slist')
