from django.shortcuts import render
from board.models import Board

def blist(request) :
    qs = Board.objects.all()
    context = {'list':qs}
    return render(request,'blist.html',context)

#글쓰기페이지 연결 : GET , 글쓰기 저장 : POST
def bwrite(request) :
    if request.method == 'GET' :
        return render(request,'bwrite.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        # bfile = request.POST.get('bfile')
        bfile = request.FILES.get('bfile')
        qs = Board(btitle=btitle,bfile=bfile)
        qs.save()

        print(f'데이터확인 : {btitle},{bfile}')
        return render(request,'bwrite.html')
        