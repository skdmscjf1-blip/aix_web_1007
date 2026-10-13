from django.shortcuts import render,redirect
from students.models import Students

#학생정보삭제
def sdelete(request,no) :
    Students.objects.get(no=no).delete()
    return redirect('students:slist')




#학생정보수정페이지,저장
def supdate (request,no) :
    if request.method=='GET':
        qs = Students.objects.get(no=no)
        context = {'stu':qs}
        return render(request,'supdate.html',context)
    elif request.method=='POST' :
        #수정부분
        qs = Students.objects.get(no=no)
        #수정된 데이터
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        #수정반영
        qs.name = name
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.hobby = hobby
        qs.save()

        return redirect('students:slist') #app_name,name 방식



#학생정보상세보기 - 1개
def sview(request,no):
    qs = Students.objects.get(no=no)
    context = {'stu':qs}
    return render(request, 'sview.html',context)


#학생정보리스트 - 여러개
def slist(request) :
    #딕셔너리 형태로 데이터를 전달함.
    qs = Students.objects.all().order_by('-no')  # 전체가져오기 , order_by() 정렬 ('-') 역순정렬
    # qs = Students.objects.get(name='홍길동')  # 1개 가져오기
    #__contains : 포함 , __endwith
    # qs = Students.objects.filter(name__contains='s')  # s가 포함되어 있는 학생
    # qs = Students.objects.filter(name__endswith='s')  # s로 끝나는학생
    # gt,gte,lt,lte
    # qs = Students.objects.filter(grade__gte=3)  # 3학년이상 학생찾기
    # qs = Students.objects.filter(grade__gt=3)  # 3학년초과 학생찾기
    context = {'list':qs}

    return render(request,'slist.html',context)



#학생정보입력페이지 - form으로 전달
def swrite(request) :
    if request.method =='GET':
        return render(request,'swrite.html')
    elif request.method == "POST" : # 1. form 값전달
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby') #checkbox 값이 여러개 list로 받아야함
        # save 저장
        qs = Students(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby)
        qs.save()
        # create저장
        # Students.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby)

        print(name,major,grade,age,gender,hobby)
        return redirect('/')

#-----------------------------------------------------------------------------------------------

# #학생정보입력페이지 - 파라미터
# def swrite3(request):
#     name = request.GET.get('name')
#     age = request.GET.get('age')
#     print(f'파라미터 값전달 : {name},{age}')
#     return redirect('/')


# #학생정보입력페이지 - url path : 매개변수로 값전달
# def swrite2(request,name):
#     print(f'값전달 : {name}')
#     return redirect('/')