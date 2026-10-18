from django.shortcuts import render
from board.models import Board

def blist(request) :
    qs = Board.objects.all()
    context = {'list':qs}    
    return render(request,'blist.html',context)

def bwrite(request) :
    if request.method == 'GET':
        return render(request,'bwrite.html')
    if request.method == 'POST':
        btitle = request.POST.get('btitle')
        bfile = request.FILES.get('bfile')
        qs = Board(btitle=btitle,bfile=bfile)
        qs.save()
        print(f'데이터확인 : {btitle},{bfile}')
        return render(request,'bwrite.html')