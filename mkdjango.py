import os
import sys


if len(sys.argv)==1:
    print("Entrer le nom du projet : ")
    projet=input()
    print("Entrer le om de votre application")
    app=input()
else:
    projet = sys.argv[1]
    app = sys.argv[2]
print("Creation du projet .....")
os.system(f"django-admin startproject {projet} ")
print("Creation de l'application .....")
os.system(f"cd {projet}")
os.system(f"cd {projet} ; django-admin startapp {app}")


def ecrire(pp, n, l):
    f = open(pp, "r")
    ll = []
    for e in f:
        ll.append(str(e))
    m = ll[:n]
    m = m[:] + l[:] + ["\n"]
    m = m[:] + ll[n:]
    f.close()
    return m




# ecrire(f, 50, l)

models = """
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to="profil/avatar/",null=True,blank=True)
    premium=models.BooleanField(default=False)
    tel1=models.CharField(max_length=12,null=True,blank=True)
    tel2=models.CharField(max_length=12,null=True,blank=True)
    tel3=models.CharField(max_length=12,null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username
"""

views = f"""
from django.shortcuts import render
from django.contrib.auth import authenticate ,login,logout
from django.urls import reverse
from django.http import JsonResponse
from {app}.forms import  RegisterForm ,LoginForm
from django.contrib.auth.models import User
from {projet}.settings import BASE_DIR
from django.shortcuts import render ,HttpResponseRedirect
from {app}.models import Profil


# Create your views here.

def index(r):
    ctx={{}}
    return render(r,"{app}/index.html",ctx)

def isconnect(r):
    if r.user.is_authenticated:
        return True
    return False

def register(r):
    ctx={{}}
    ctx['error']=[]
    if r.method=="POST":
        form=RegisterForm(r.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            # lastname=form.cleaned_data['lastname']
            email=form.cleaned_data['email']
            pwd1=form.cleaned_data['pwd1']
            pwd2=form.cleaned_data['pwd2']
            tel1=form.cleaned_data['tel1']
            tel2=form.cleaned_data['tel2']
            tel3=form.cleaned_data['tel3']

            if pwd1==pwd2:
                user=User.objects.create_user(username=username,first_name="",last_name="",email=email,password=pwd1)
                profil=Profil()
                profil.user=user
                profil.tel1=tel1
                profil.tel2=tel2
                profil.tel3=tel3
                profil.save()
                # creer_dossier_user(username)
                return HttpResponseRedirect(reverse('index'))
            else:
                ctx['error'].append('les mots de pass ne sont pas identiques')
                ctx['form']=form
                return render(r,"{app}/register.html",ctx)

    else:
        form=RegisterForm()

    ctx['form']=form
    return render(r,"{app}/register.html",ctx)

def login_u(r):
    ctx={{
        'data':''
    }}
    if r.method=="POST":
        form=LoginForm(r.POST)
        if form.is_valid():

            username=form.cleaned_data['username']
            password=form.cleaned_data['pwd']

            user=authenticate(r,username=username,password=password)
            if user is not None:
                login(r,user)
                ctx['user']=user
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('register'))
    else:
        form=LoginForm()
        ctx['form']=form
    return render(r,"{app}/login.html",ctx)



def logout_user(r):
    logout(r)
    return HttpResponseRedirect(reverse('index'))

def view_404(request, *args, **kwargs):
    return render(request,'{app}/404.html',{{}})

def view_500(request, *args, **kwargs):
    return render(request,'{app}/500.html',{{}})


"""

forms = """
from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':"Votre nom d'utilisateur",'label':''}))
    # lastname=forms.CharField(max_length=150)
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'john@gmail.com'}))
    pwd1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Votre mot de pass'}))
    pwd2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Repeter le mot de pass"}))
    tel1=forms.CharField(max_length=12,required=False,widget=forms.TextInput(attrs={'placeholder':"77 000 00 00( optionnel)"}))
    tel2=forms.CharField(max_length=12,required=False,widget=forms.TextInput(attrs={'placeholder':"76 000 00 00( optionnel)"}))
    tel3=forms.CharField(max_length=12,required=False,widget=forms.TextInput(attrs={'placeholder':"70 000 00 00( optionnel)"}))



class LoginForm(forms.Form):
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':"Nom d'utilisateur"}))
    pwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Votre mot de pass"}))

"""

os.mkdir(f"{projet}/{app}/templates")
os.mkdir(f"{projet}/{app}/templates/{app}")


with open(f"{projet}/{app}/models.py", "w") as f:
    # v = models.split("\n")
    # for e in v:
    f.write(models)

with open(f"{projet}/{app}/forms.py", "w") as f:
    # v = models.split("\n")
    # for e in v:
    f.write(forms)


with open(f"{projet}/{app}/views.py", "w") as f:
    # v = views.split("\n")
    # for e in v:
    f.write(views)


f = open(f"{projet}/{app}/templates/{app}/index.html", "w")
ht = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{app}</title>
</head>
<body>
    <h1>Bienvenue</h1>
</body>
</html>

"""
f.write(ht)
f.close()
print("Creation des fichiers inde.html 404.html 500.html register.html login.html")

open(f"{projet}/{app}/templates/{app}/404.html", "w")
open(f"{projet}/{app}/templates/{app}/500.html", "w")
open(f"{projet}/{app}/templates/{app}/register.html", "w")
open(f"{projet}/{app}/templates/{app}/login.html", "w")


def chg(pp, n, l):
    d = ecrire(pp, n, l)
    with open(pp, "w") as f:
        for e in d:
            f.write(e)

l = [f'    "{app}.apps.{app.title()}Config",']
print("Ajout de l'application dans setting.py .......")
chg(f"./{projet}/{projet}/settings.py", 39, l)
print("Creation de l'url d'accueil ......")
chg(f"./{projet}/{projet}/urls.py", 18, [f"from {app} import views"])
chg(f"./{projet}/{projet}/urls.py", 22, ['    path("", view=views.index),'])

os.system(f"python {projet}/manage.py makemigrations")
os.system(f"python {projet}/manage.py migrate")
print("Creer un administrateur principal qui a tout les pouvoirs ....")
os.system(f"python {projet}/manage.py createsuperuser")
ok=input("Voulez vous lancer le serveur de production:y/N ")

if ok=='y':
    os.system(f"python {projet}/manage.py runserver")

print("Fin ... Enjoy")
