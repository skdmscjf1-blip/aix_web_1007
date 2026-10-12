from django.shortcuts import render,redirect
from students.models import Students

#학생정보삭제
def sdelete (request,name):
    Students.objects.get(name=name).delete()
    return redirect('/students/slist/')


#학생정보수정
def supdate (request,name):
    if request.method =='GET' :
        qs = Students.objects.get(name=name)
        context = {'stu':qs}
        return render(request,'supdate.html',context)
    elif request.method =='POST' :
        qs = Students.objects.get(name=name)
        if qs :
            name = request.POST.get('name')
            major= request.POST.get('major')
            age = request.POST.get('age')
            grade = request.POST.get('grade')
            gender = request.POST.get('gender')

            qs.name = name
            qs.major = major
            qs.age = age
            qs.grade = grade
            qs.gender = gender
            qs.save()
        return redirect('/students/slist/')

#학생상세정보
def sview(request,name) :
    qs = Students.objects.get(name=name)
    context = {'stu':qs}

    return render(request, 'sview.html',context)

#학생성적리스트
def slist(request) :
    qs = Students.objects.all()
    context = {'list':qs}

    return render(request, 'slist.html',context)

#학생성적입력
def swrite(request) :
    if request.method == 'GET' :
        print("GET 페이지 출력")
        return render(request, 'swrite.html')
    elif request.method =='POST' :
        print('POST 페이지 출력')
        name = request.POST.get('name')
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')

        qs = Students(name=name,major=major,age=age,grade=grade,gender=gender)
        qs.save()
        print(name,major,age,grade,gender)
        return redirect('/')

    
