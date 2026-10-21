from django.shortcuts import render
from player.models import Player

def plist(request) :
    qs = Player.objects.all()

    context = {'list':qs}

    return render(request,'plist.html',context)