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
from member.models import Member
from event.models import Event


def commWrite(request):
    eno = request.POST.get('eno')
    e_qs = Event.objects.get(eno=eno)
    m_qs = Member.objects.get(id=request.session['session_id'])

    cpw = request.POST.get('cpw')
    ccontent = request.POST.get('ccontent')

    qs = Comment.objects.create(event=e_qs,member=m_qs,cpw=cpw,ccontent=ccontent)
    qs_1 = Comment.objects.filter(cno=qs.cno).values()
    qs_1 = list(qs_1)

    print(f'확인 : {eno},{cpw},{ccontent},{qs.cno},{qs.cdate},')
    context ={'result':'성공','comment':qs_1}
    return JsonResponse(context)
        

def commlist(request):
    context = {'result':'성공'}
    return JsonResponse(context)