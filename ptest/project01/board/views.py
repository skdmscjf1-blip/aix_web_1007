from django.shortcuts import render,redirect
from django.db.models import F,Q
from board.models import Board
from django.conf import settings
from django.conf.urls.static import static
import os
from member.models import Member
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#글삭제
def bdelete(request,bno):
    qs = Board.objects.get(bno=bno)

    # 파일삭제 c:/upload/board/1.jpg ------
    media_root = settings.MEDIA_ROOT
    remove_file = media_root+"/"+str(qs.bfile)
    if os.path.isfile(remove_file):
        os.remove(remove_file)
    #--------------------------------------    

    qs.delete()

    context = {'temp':0,'bno':bno}

    return render(request,'bwrite.html',context)


#글수정
def bupdate(request,bno):
    if request.method =='GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request, 'bupdate.html',context)
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        if bfile:
            qs.bfile = bfile
        qs.save()

        context={'temp':2,'bno':bno}
        return render(request, 'bwrite.html',context)


# 게시글 작성
def bwrite(request):
    if request.method =='GET':
        return render(request,'bwrite.html')
    elif request.method =='POST':
        btitle = request.POST.get('btitle')
        id = request.session['session_id']
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        print(f'데이터확인 : {btitle},{id},{bcontent},{bfile}')
        member = Member.objects.get(id=id)
        qs = Board.objects.create(btitle=btitle,member=member,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'temp':1}
        return render(request,'bwrite.html',context)
#게시글 상세
def bview (request,bno):
    page = int(request.GET.get('page',1))
    qs = Board.objects.filter(bno=bno).first()
    qs.bhit = qs.bhit + 1
    qs.save()

    pre_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep) |\
            Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by('-bgroup','bstep').first()
    next_qs = Board.objects.filter(Q(bgroup__gt=qs.bgroup,bstep__gte=qs.bstep) |\
            Q(bgroup=qs.bgroup,bstep__lt=qs.bstep)).order_by('-bgroup','bstep').first()
    context = {'board':qs,'pre_board':pre_qs,'next_board':next_qs,'page':page}
    return render(request,'bview.html',context)
#게시글 리스트
def blist(request):
    if request.method =='GET':
        qs = Board.objects.all().order_by('-bgroup','bstep')
        paginator = Paginator(qs,5)
        page = int(request.GET.get('page',1))
        p_qs = paginator.get_page(page)
        context = {'list':p_qs,'page':page}
        return render(request,'blist.html',context)
    if request.method == 'POST':
        category = request.POST.get('category')
        search_word = request.POST.get('search_word')
        if category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search_word).order_by('-bgroup','bstep')
        elif category == 'bcontent':
            qs = Board.objects.filter(bcontent__contains=search_word).order_by('-bgroup','bstep')
        else:
            qs = Board.objects.filter(Q(btitle__contains=search_word) | Q(bcontent__contains=search_word)).order_by('-bgroup','bstep')




        paginator = Paginator(qs,5)
        page = int(request.GET.get('page',1))
        p_qs = paginator.get_page(page)
        context = {'list':p_qs,'page':page}
        return render(request,'blist.html',context)
