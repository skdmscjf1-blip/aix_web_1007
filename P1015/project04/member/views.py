from django.shortcuts import render,redirect
from member.models import Member

def logout(request):
    request.session.clear()
    context = {'temp':2}
    return render(request,'login.html',context)

def login(request) :
    if request.method =='GET':
        cook_id = request.COOKIES.get('cook_id','')
        context ={'cook_id':cook_id}
        return render(request,'login.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        rememberId = request.POST.get('rememberId')
        qs = Member.objects.filter(id=id,pw=pw).first()
        if qs :
            request.session['se_id'] = qs.id
            request.session['se_nickname'] = qs.nickname
            context = {'temp':1}
        else :
            context = {'temp':0}
        response = render(request,'login.html',context)

        if rememberId:
            response.set_cookie('cook_id',id,max_age=60*60)
        else:
            response.delete_cookie('cook_id')

        return response