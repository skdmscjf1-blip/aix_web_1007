from django.shortcuts import render,redirect
from member.models import Member


def mupdate(request,id) :
    if request.method == 'GET':
        qs = Member.objects.get(id=id)
        tel = qs.tel.split('-')
        context = {'member':qs,'tel':tel}
        print(f'데이터확인 :{id},{tel}')
        return render (request,'mupdate.html',context)
    elif request.method == 'POST' :
        # id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        tel3 = request.POST.get('tel3')
        tel = f'{tel1}-{tel2}-{tel3}'
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')

        qs = Member.objects.get(id=id)
        qs.pw = pw
        qs.name = name
        qs.nickname = nickname
        qs.tel = tel
        qs.gender = gender
        qs.hobby = hobby
        qs.save()
        request.session['se_nickname'] = qs.nickname

        print(f'{id},{pw},{name},{nickname},{tel},{gender},{hobby}')
        return redirect('/')




def mwrite(request) :
    if request.method =='GET' :
        return render(request,'mwrite.html')
    elif request.method == 'POST' :
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        tel3 = request.POST.get('tel3')
        tel = f'{tel1}-{tel2}-{tel3}'
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        print(f'데이터확인 : {id},{pw},{name},{nickname},{tel},{gender},{hobby}')
        qs = Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)
        qs.save()
        return render(request,'mresult.html')


def logout(request) :
    request.session.clear()
    context = {'temp':2}
    return render(request,'login.html',context)

# Create your views here.
def login(request) :
    if request.method == 'GET' :
        cook_id = request.COOKIES.get('cook_id','')
        if cook_id:
            context={'cook_id':cook_id}
        else:
            context = {}
        return render(request,'login.html',context)
    elif request.method == 'POST' :
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        rememberId = request.POST.get('rememberId')
        qs = Member.objects.filter(id=id,pw=pw).first()
        if qs :
            context = {'temp':1}
            request.session['se_id'] = qs.id
            request.session['se_nickname'] = qs.nickname
        else :
            context = {'temp':0}
        print(f'데이터 : {id},{pw},{rememberId},{context}')
        response = render(request,'login.html',context)
        if rememberId :
            response.set_cookie('cook_id',id,max_age=60*60*24*365)
        else:
            response.delete_cookie('cook_id')
        return response


