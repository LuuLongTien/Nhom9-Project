from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router =DefaultRouter();
router.register('champion', views.APIChampion)

urlpatterns = [
    path('register/',views.Register, name = 'register'),
    path('search/info/',views.ChampionInfo, name = 'info'), #info tuong
    path('search/', views.SearchBar, name = 'search'), #trang search
    # path('teambuild/', views.TeamBuilding, name = 'teambuild'), #trang build team
    # path('team/',views.TeamName, name = 'name'), # trang tao team name
    #path('save/', views.Save, name = 'save'),
    path('api/',include(router.urls)),
    # path('base/',views.Base, name = 'base'),
    path('class/', views.MainPage, name = 'class'),
    path('index/',views.index, name = 'index'),    # path('getteamname/',views.TeamName, name = 'teamname'),
    path('login/', views.Login, name = 'login'),
    path('logout/', views.Logout, name = 'logout'),
    path('meta/',views.Meta, name = 'meta'),
    path('item/',views.ItemShow, name = 'item'),
    path('profile/',views.UserProfile, name = 'profile'),
    path('linhthu/',views.LinhThu, name ='linhthu'),
    path('aboutuser/', views.UserInfo, name = 'auser'),
    path('userchange/',views.UserFix, name ='userfix')
]
