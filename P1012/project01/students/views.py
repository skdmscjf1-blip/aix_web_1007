from django.shortcuts import render,redirect
from students.models import Stu

def sdelete(request,name) :
    Stu.objects.get(name=name).delete()
    return redirect('/students/slist/')


#학생상세보기
def sview(request,name) : 
    print(f'name 데이터 : {name}')
    qs = Stu.objects.get(name=name) #1개의 정보전송
    context = {'stu':qs}

    return render(request,'sview.html',context)

#학생정보수정
def supdate(request,name) : 
    if request.method=='GET':
        print(f'name 수정페이지 : {name}')
        qs = Stu.objects.get(name=name) #1개의 정보전송
        context = {'stu':qs}

        return render(request,'supdate.html',context)
    elif request.method == 'POST' :
        print(f'name 수정완료 : {name}')
        qs = Stu.objects.get(name=name) # 이전정보 검색
        if qs :
            name = request.POST.get('name')
            major = request.POST.get('major')
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



#학생정보리스트
def slist(request) :
    #db에서 전체리스트 가져오기
    qs = Stu.objects.all() #전체가져오기

    # qs = Stu.objects.get(name='홍길동') #1개
    # qs = Stu.objects.filter(name__contains='홍')  #검색해서 여러개


    context = {'list':qs}
    return render(request, 'slist.html',context)

#학생성적입력페이지,저장
def swrite(request) :
    if request.method =='GET' :
        return render(request, 'swrite.html')
    elif request.method == 'POST' :
        name = request.POST.get('name') #데이터가 없어도 에러가 나지 않음
        # major = request.POST['major'] #데이터가 없을때 에러남
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')
        # 1. save()
        qs = Stu(name=name,major=major,age=age,grade=grade,gender=gender)
        qs.save()
        # 2. create()
        # Stu.objects.create(name=name,major=major,age=age,grade=grade,gender=gender)

        print(f'확인 : {name},{major}')
        return redirect('/students/slist')


