from queue import Empty
from tkinter import CASCADE
from tokenize import Special
from turtle import ondrag
from django.db import models
from django.forms import CharField

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=50, default='Your username')
    Password = models.CharField(max_length=100, blank = False, null = False)
    Email = models.CharField(max_length=200, blank = True, null = True)
    Avatar = models.ImageField()
    def __str__(self):
        return self.Username

class TeamBuilder(models.Model):
    Player = models.ForeignKey(User, on_delete=models.CASCADE)
    TeamName = models.CharField(max_length = 50)
    def __str__(self):
        return self.TeamName

class Champion(models.Model):
    Team = models.ManyToManyField(TeamBuilder)
    Name = models.CharField(max_length=30)
    Image = models.ImageField()
    CLASSES = (
        ('Innovator', 'Innovator'),
        ('Assassin', 'Assassin'),
        ('Scholar', 'Scholar'),
        ('Sniper', 'Sniper'),
        ('Striker', 'Striker'),
        ('Transformer', 'Transformer'),
        ('Bruiser', 'Bruiser'),
        ('Challenger', 'Challenger'),
        ('Colossus', 'Colossus'),
        ('Enchanter', 'Enchanter'),
        ('Twinshot', 'Twinshot'),
        ('Arcanist', 'Arcanist'),
        ('Bodyguard', 'Bodyguard'),
    )
    Class = models.CharField(max_length=100,choices = CLASSES)
    ORIGIN = (
        ('Enforcer', 'Enforcer'),
        ('Glutton', 'Glutton'),
        ('Mastermind', 'Mastermind'),
        ('Rival', 'Rival'),
        ('Socialite', 'Socialite'),
        ('Yordle-Lord', 'Yordle-Lord'),
        ('Debonair', 'Debonair'),
        ('Scrap', 'Scrap'),
        ('Chemtech', 'Chemtech'),
        ('Clockwork', 'Clockwork'),
        ('Mutant', 'Mutant'),
        ('Syndicate', 'Syndicate'),
        ('Hextech', 'Hextech'),
        ('Mercenary', 'Mercenary'),
        ('Yordle', 'Yordle'),
    )
    Origin = models.CharField(max_length=100, choices= ORIGIN)
    Special = models.CharField(max_length=100, default=Empty, blank= True, null = True)
    Money = models.IntegerField(default = 0)
    def __str__(self):
        return self.Name


class Item(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField()
    Recipe1 = (
        ('B.F.Sword', 'B.F.Sword'),
        ('ChainVest', 'ChainVest'),
        ('GiantsBelt', 'GiantsBelt'),
        ('NeedlesslyLargeRod', 'NeedlesslyLargeRod'),
        ('NegatronCloak', 'NegatronCloak'),
        ('RecurveBow', 'RecurveBow'),
        ('SparringGloves', 'SparringGloves'),
        ('Spatula', 'Spatula'),
        ('TearoftheGoddess', 'TearoftheGoddess'),
    )
    Recipe2 = (
        ('B.F.Sword', 'B.F.Sword'),
        ('ChainVest', 'ChainVest'),
        ('GiantsBelt', 'GiantsBelt'),
        ('NeedlesslyLargeRod', 'NeedlesslyLargeRod'),
        ('NegatronCloak', 'NegatronCloak'),
        ('RecurveBow', 'RecurveBow'),
        ('SparringGloves', 'SparringGloves'),
        ('Spatula', 'Spatula'),
        ('TearoftheGoddess', 'TearoftheGoddess'),
    )
    MadeFrom1=models.CharField(max_length=100, default=Empty, choices= Recipe1)
    MadeFrom2=models.CharField(max_length=100, default=Empty, choices= Recipe2)
    def __str__(self):
        return self.Name
