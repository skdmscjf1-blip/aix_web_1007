from django.shortcuts import render
from board.models import Board


def blist(request):
    qs = Board.objects.all().order_by('-bgroup','bstep')
    context={'list':qs}
    return render(request,'blist.html',context)


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
        context


def bdelete(request,bno):
    qs = Board.objects.get(bno=bno).delete()
    context = {'temp':0,'bno':bno}
    return render(request,'bwrite.html',context)


def bview(request,bno):
    qs = Board.objects.filter(bno=bno)
    context = {'board':qs[0]}
    return render(request,'bview.html',context)