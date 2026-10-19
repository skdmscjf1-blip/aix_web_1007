from django.shortcuts import render,redirect
from django.db.models import F,Q
from board.models import Board

#게시글 삭제
def bdelete(request,bno):
    Board.objects.get(bno=bno).delete()
    context = {'temp':0,'bno':bno}
    return render(request,'bwrite.html',context)

def bupdate(request,bno) :
    if request.method =='GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'bupdate.html',context)
    elif request.method =='POST' :
        btitle = request.POST.get('btitle')
        # id = request.POST.get('id')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        if bfile :
            qs.bfile = bfile
        qs.save()
        context = {'temp':2,'bno':bno}
        return render(request,'bwrite.html',context)

#게시글 리스트
def blist(request):
    qs = Board.objects.all().order_by('-bgroup','bstep')
    context={'list':qs}
    return render(request,'blist.html',context)

#게시글 등록
def bwrite(request):
    if request.method =='GET':
        return render(request,'bwrite.html')
    if request.method =='POST':
        btitle = request.POST.get('btitle')
        id = request.POST.get('id')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        qs = Board(btitle=btitle,id=id,bcontent=bcontent,bfile=bfile)
        qs.save()
        #답변달기
        qs.bgroup = qs.bno
        qs.save()
        context = {'temp':1}
        return render(request,'bwrite.html',context)



#게시글 상세보기
def bview(request,bno):
    qs = Board.objects.filter(bno=bno)
    qs.update(bhit = F('bhit')+1)
    context = {'board':qs[0]}
    return render(request,'bview.html',context)