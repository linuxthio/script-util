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
from django.db import models  \n
from django.contrib.auth.models import User \n
# Create your models here. \n
 \n
class Profil(models.Model): \n
    user=models.OneToOneField(User,on_delete=models.CASCADE) \n
    avatar=models.ImageField(upload_to="profil/avatar/",null=True,blank=True) \n
    premium=models.BooleanField(default=False) \n
    tel1=models.CharField(max_length=12,null=True,blank=True) \n
    tel2=models.CharField(max_length=12,null=True,blank=True) \n
    tel3=models.CharField(max_length=12,null=True,blank=True) \n
 \n
    def __str__(self) -> str: \n
        return self.user.username \n
"""

views = f"""
from django.shortcuts import render \n
from django.contrib.auth import authenticate ,login,logout \n
from django.urls import reverse \n
from django.http import JsonResponse \n
from {app}.forms import  RegisterForm ,LoginForm \n
from django.contrib.auth.models import User \n
from {projet}.settings import BASE_DIR \n
from django.shortcuts import render ,HttpResponseRedirect \n
from {app}.models import Profil \n
 \n
 \n
# Create your views here. \n
 \n
def index(r): \n
    ctx={{}} \n
    return render(r,"{app}/index.html",ctx) \n
 \n
def isconnect(r): \n
    if r.user.is_authenticated: \n
        return True \n
    return False \n
 \n
def register(r): \n
    ctx={{}} \n
    ctx['error']=[] \n
    if r.method=="POST": \n
        form=RegisterForm(r.POST) \n
        if form.is_valid(): \n
            username=form.cleaned_data['username'] \n
            # lastname=form.cleaned_data['lastname'] \n
            email=form.cleaned_data['email'] \n
            pwd1=form.cleaned_data['pwd1'] \n
            pwd2=form.cleaned_data['pwd2'] \n
            tel1=form.cleaned_data['tel1'] \n
            tel2=form.cleaned_data['tel2'] \n
            tel3=form.cleaned_data['tel3'] \n
 \n
            if pwd1==pwd2: \n
                user=User.objects.create_user(username=username,first_name="",last_name="",email=email,password=pwd1) \n
                profil=Profil() \n
                profil.user=user \n
                profil.tel1=tel1 \n
                profil.tel2=tel2 \n
                profil.tel3=tel3 \n
                profil.save() \n
                # creer_dossier_user(username) \n
                return HttpResponseRedirect(reverse('index')) \n
            else: \n
                ctx['error'].append('les mots de pass ne sont pas identiques') \n
                ctx['form']=form \n
                return render(r,"{app}/register.html",ctx) \n
 \n
    else: \n
        form=RegisterForm() \n
 \n
    ctx['form']=form \n
    return render(r,"{app}/register.html",ctx) \n
 \n
def login_u(r): \n
    ctx={{ \n
        'data':'' \n
    }}\n
    if r.method=="POST": \n
        form=LoginForm(r.POST) \n
        if form.is_valid(): \n
 \n
            username=form.cleaned_data['username'] \n
            password=form.cleaned_data['pwd'] \n
 \n
            user=authenticate(r,username=username,password=password) \n
            if user is not None: \n
                login(r,user) \n
                ctx['user']=user \n
                return HttpResponseRedirect(reverse('index')) \n
            else: \n
                return HttpResponseRedirect(reverse('register')) \n
    else: \n
        form=LoginForm() \n
        ctx['form']=form \n
    return render(r,"{app}/login.html",ctx) \n
 \n
 \n
 \n
def logout_user(r): \n
    logout(r) \n
    return HttpResponseRedirect(reverse('index')) \n
 \n
def view_404(request, *args, **kwargs): \n
    return render(request,'{app}/404.html',{{}}) \n
 \n
def view_500(request, *args, **kwargs): \n
    return render(request,'{app}/500.html',{{}}) 
\n    
"""

forms = """
from django import forms\n

class RegisterForm(forms.Form): \n
    username=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':"Votre nom d'utilisateur",'label':''}))\n
    # lastname=forms.CharField(max_length=150)\n
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'john@gmail.com'}))\n
    pwd1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Votre mot de pass'}))\n
    pwd2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Repeter le mot de pass"}))\n
    tel1=forms.CharField(max_length=12,required=False,widget=forms.TextInput(attrs={'placeholder':"77 000 00 00( optionnel)"}))\n
    tel2=forms.CharField(max_length=12,required=False,widget=forms.TextInput(attrs={'placeholder':"76 000 00 00( optionnel)"}))\n
    tel3=forms.CharField(max_length=12,required=False,widget=forms.TextInput(attrs={'placeholder':"70 000 00 00( optionnel)"}))\n



class LoginForm(forms.Form): \n
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':"Nom d'utilisateur"}))\n
    pwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Votre mot de pass"}))\n
\n

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