from ast import Or
from msilib.schema import Class
import re
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Origin
from .models import Champion
import json
# Create your views here.
from getchamp.serializers import *
from rest_framework import viewsets
def TestView(request):
    return HttpResponse("Hello world")


def ImageTest(request):
    q = Champion.objects.all()
    if 'a' in request.GET:
        a = request.GET['a']
        post = Champion.objects.filter(Name__icontains = a)
    else:
        post = Champion.objects.all()
    return render(request, 'getchamp/index.html', {'q':q})

def SearchBar(request):
    #Search by name
    if 'a' in request.GET:
        a = request.GET['a']
        post = Champion.objects.filter(Name__icontains = a)
    else:
        post = Champion.objects.all()
    
    #Origin Filter
    tmp =  str(list(request.GET.keys()))
    tmp = tmp[3:-2]
    tmp = "b"+tmp
    if tmp in request.GET:
        b =  str(list(request.GET.keys()))
        b = b[3:-2]
        post  = Champion.objects.filter(Origin = b)

    
    #Class filter
    cl = str(list(request.GET.keys()))
    cl = cl[3:-2]
    cl = "c" + cl
    if cl in request.GET:
        c = str(list(request.GET.keys()))
        c = c[3:-2]
        post = Champion.objects.filter(Class = c)

    return render(request, 'getchamp/all_champion.html',{'post': post})



def TeamBuilding(request):
    #Search by name
    if 'a' in request.GET:
        a = request.GET['a']
        post = Champion.objects.filter(Name__icontains = a)
    else:
        post = Champion.objects.all()
    
    #Origin Filter
    tmp =  str(list(request.GET.keys()))
    tmp = tmp[3:-2]
    tmp = "b"+tmp
    if tmp in request.GET:
        b =  str(list(request.GET.keys()))
        b = b[3:-2]
        post  = Champion.objects.filter(Origin = b)

    
    #Class filter
    cl = str(list(request.GET.keys()))
    cl = cl[3:-2]
    cl = "c" + cl
    if cl in request.GET:
        c = str(list(request.GET.keys()))
        c = c[3:-2]
        post = Champion.objects.filter(Class = c)
    team = TeamBuilder.objects.all()
    tem = Champion.objects.filter(Name = 'Jinx')
    if 'iname' in request.GET:
        iname = request.GET['iname']
        tem = Champion.objects.filter(Name = iname)

    b = TeamBuilder.objects.filter(pk =1 )
    return render(request, 'getchamp/teambuilder.html',{'post': post, 'team': team,'tem':tem})

#API
class APIChampion(viewsets.ModelViewSet):
    queryset = Champion.objects.filter()
    serializer_class = ChampionSerializer

#hien thong tin ve tuong khi click vao
def ChampionInfo(request):
    info = request.GET['xname']
    post = Champion.objects.filter(Name = info)
    return render(request, 'getchamp/champion_info.html', {'post':post})
#Tao team name
def TeamName(request):
    if 'text' in request.GET:
        team = request.GET['text']
        team.replace('+',' ')
        user = User.objects.get(pk = 1)
        b = TeamBuilder(TeamName = team, Player = user)
        b.save()
        return redirect('/app/teambuild')
    return render(request, 'getchamp/create_team_name.html')
