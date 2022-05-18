from ast import Or
from email.policy import HTTP
from http.client import HTTPResponse
from msilib.schema import Class
import re
# from readline import redisplay
from turtle import title
import django
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Origin
from .models import Champion, Item
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm
from django.contrib import messages
import json
# Create your views here.
from getchamp.serializers import *
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

def Register(request):
    if request.user.is_authenticated:
        return redirect('search')
    else:
        form = CreateUserForm()
        if request.method ==  'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for: ' + user)
                return redirect('login')
        return render(request, 'getchamp/register.html',{'form': form})


def Login(request):
    if request.user.is_authenticated:
        return redirect('search')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'getchamp/login.html',context)

def Logout(request):
    logout(request)
    return redirect('login')

def ImageTest(request):
    q = Item.objects.all()
    if 'a' in request.GET:
        a = request.GET['a']
        post = Champion.objects.filter(Name__icontains = a)
    else:
        post = Champion.objects.all()
    return render(request, 'getchamp/index.html', {'q':q})

@login_required(login_url='login')
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
    
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})

    return render(request, 'getchamp/all_champion.html',{'post': post})


@login_required(login_url='login')
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
@login_required(login_url='login')
def ChampionInfo(request):
    info = request.GET['xname']
    post = Champion.objects.filter(Name = info)
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request, 'getchamp/champion_info.html', {'post':post})


#Tao team name
@login_required(login_url='login')
def TeamName(request):
    if 'text' in request.GET:
        team = request.GET['text']
        team.replace('+',' ')
        user = User.objects.get(pk = 1)
        b = TeamBuilder(TeamName = team, Player = user)
        b.save()
        return redirect('/app/teambuild')
    return render(request, 'getchamp/create_team_name.html')


def index(request):
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request,'getchamp/main.html')
# def Base(request):
#     return render(request, 'getchamp/base.html')

@login_required(login_url='login')
def MainPage(request):
    thachdau = Champion.objects.filter(Class = 'Challenger')
    thuatsu = Champion.objects.filter(Class = 'Enchanter')
    vesi = Champion.objects.filter(Class = 'Bodyguard')
    lienxa = Champion.objects.filter(Class = 'Twinshot')
    satthu = Champion.objects.filter(Class = 'Assassin')
    nhaphatminh = Champion.objects.filter(Class = 'Innovator')
    phapsu = Champion.objects.filter(Class = 'Arcanist')
    xathu = Champion.objects.filter(Class = 'Sniper')
    tiencong = Champion.objects.filter(Class = 'Striker')
    chuyendang = Champion.objects.filter(Class = 'Transformer')
    dausi = Champion.objects.filter(Class = 'Bruiser')
    hocgia = Champion.objects.filter(Class = 'Scholar')
    khonglo = Champion.objects.filter(Class = 'Colossus')
    doithu = Champion.objects.filter(Origin = 'Rival')
    bangdang = Champion.objects.filter(Origin = 'Syndicate')
    yordle = Champion.objects.filter(Origin = 'Yordle')
    taiche = Champion.objects.filter(Origin = 'Scrap')
    trumyordle = Champion.objects.filter(Origin = 'Yordle-Lord')
    thantuong = Champion.objects.filter(Origin = 'Socialite')
    dotbien = Champion.objects.filter(Origin = 'Mutant')
    ngoaibinh = Champion.objects.filter(Origin = 'Mercenary')
    phaman = Champion.objects.filter(Origin = 'Glutton')
    congnghe = Champion.objects.filter(Origin = 'Hextech')
    thanhlich = Champion.objects.filter(Origin = 'Debonair')
    maymoc = Champion.objects.filter(Origin = 'Clockwork')
    canhbinh = Champion.objects.filter(Origin = 'Enforcer')
    hoaky = Champion.objects.filter(Origin = 'Chemtech')
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request, 'getchamp/class_origin.html',{'thachdau':thachdau, 'thuatsu':thuatsu,'vesi':vesi,
    'lienxa':lienxa, 'satthu':satthu, 'phatminh':nhaphatminh, 'phapsu':phapsu,'xathu':xathu,'tiencong':tiencong,'chuyendang':chuyendang,
    'dausi':dausi, 'hocgia':hocgia,'khonglo':khonglo,'doithu':doithu,'bangdang':bangdang,'yordle':yordle,'taiche':taiche,'trumyordle':trumyordle,
    'thantuong':thantuong,'dotbien':dotbien, 'ngoaibinh':ngoaibinh,'phaman':phaman,'congnghe':congnghe, 'thanhlich':thanhlich,
    'maymoc':maymoc,'canhbinh':canhbinh,'hoaky':hoaky})

@login_required(login_url='login')
def Meta(request):
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request, 'getchamp/meta.html')


@login_required(login_url='login')
def ItemShow(request):
    post = Item.objects.all()
    if 'a' in request.GET:
        a = request.GET['a']
        post = Item.objects.filter(Name__icontains = a)
    else:
        post = Item.objects.all()
    item = Item.objects.all()
    if 'item' in request.GET:
        item = request.GET['item']
        post = Item.objects.filter(Q(MadeFrom1=item) | Q(MadeFrom2=item))
    
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request, 'getchamp/item.html',{'post':post})

@login_required(login_url='login')
def UserInfo(request):
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request, 'getchamp/all_user.html',{'anyone':anyone})


@login_required(login_url='login')
def UserProfile(request):
    args = {'user': request.user}
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request,'getchamp/profile.html',args)


@login_required(login_url='login')
def LinhThu(request):
    anyone = User.objects.all()
    if 'search' in request.GET:
        a = request.GET['search']
        anyone = User.objects.filter(username__icontains = a)
        return render(request, 'getchamp/all_user.html',{'anyone':anyone})
    if 'button1' in request.GET:
        b = request.GET['button1']
        depth = User.objects.filter(username = b)
        return render(request, 'getchamp/profile2.html', {'user':depth})
    return render(request, 'getchamp/linhthu.html')

@login_required(login_url='login')
def UserFix(request):
    if request.method ==  'POST':
            form = UserUpdateForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was updated')
                return redirect('profile')
            else:
                messages.MessageFailure(request, 'Account wasnt updated')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'getchamp/user_profile_change.html',{'p':form})