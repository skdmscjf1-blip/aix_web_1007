from django.shortcuts import render
from player.models import Player

def plist(request) :
    qs = Player.objects.all()
    context = {'list':qs}
    return render(request,'plist.html',context)

def pview(request,id):
    qs = Player.objects.get(id=id)
    context = {'player':qs}
    return render(request,'pview.html',context)