import os
import sys

projet = sys.argv[1]
app = sys.argv[2]

os.system(f"django-admin startproject {projet} .")
os.system(f"django-admin startapp {app}")


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


l = [f'    "{app}.apps.{app.title()}Config",']

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
from app1.forms import  RegisterForm ,LoginForm \n
from django.contrib.auth.models import User \n
from test2.settings import BASE_DIR \n
from django.shortcuts import render ,HttpResponseRedirect \n
from app1.models import Profil \n
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

os.mkdir(f"{app}/templates")
os.mkdir(f"{app}/templates/{app}")


with open(f"{app}/models.py", "w") as f:
    # v = models.split("\n")
    # for e in v:
    f.write(models)

with open(f"{app}/views.py", "w") as f:
    # v = views.split("\n")
    # for e in v:
    f.write(views)


open(f"{app}/templates/{app}/index.html", "w")
open(f"{app}/templates/{app}/404.html", "w")
open(f"{app}/templates/{app}/500.html", "w")
open(f"{app}/templates/{app}/register.html", "w")
open(f"{app}/templates/{app}/login.html", "w")


def chg(pp, n, l):
    d = ecrire(pp, n, l)
    with open(pp, "w") as f:
        for e in d:
            f.write(e)


chg(f"./{projet}/settings.py", 39, l)
chg(f"./{projet}/urls.py", 18, [f"from {app} import views"])
chg(f"./{projet}/urls.py", 22, ['    path("", view=views.index),'])
