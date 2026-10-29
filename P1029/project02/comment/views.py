import os
from pathlib import Path
from dotenv import load_dotenv
from django.db.models import F,Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.text import MIMEText
import random
import string
from comment.models import Comment
from event.models import Event
from member.models import Member



# 댓글삭제
def commDelete(request):
    cno = request.POST.get('cno')
    print('삭제할 댓글번호 : ', cno)   # ★ 추가
    Comment.objects.get(cno=cno).delete()
    context = {'result':'성공'}
    return JsonResponse(context)

def commlist(request):
    context = {'result':'성공'}
    return JsonResponse(context)

# ajax 댓글쓰기
def commWrite(request):
    eno = request.POST.get('eno',)
    # ForeignKey 는 객체1개 전체를 입력해야 함.
    e_qs = Event.objects.get(eno=eno)
    m_qs = Member.objects.get(id=request.session['session_id'])

    cpw = request.POST.get('cpw','')
    ccontent = request.POST.get('ccontent')
    #Comment 저장 - qs : cno,event,member,cpw,ccontent,cdate
    qs = Comment.objects.create(event=e_qs,member=m_qs,cpw=cpw,ccontent=ccontent)
    # Json 타입으로 변경
    qs_1 = Comment.objects.filter(cno=qs.cno).values()
    qs_1 = list(qs_1)
    print(f'확인 : {eno},{cpw},{ccontent},{qs.cno},{qs.cdate}')
    context = {'result':'성공','comment':qs_1}
    return JsonResponse(context)