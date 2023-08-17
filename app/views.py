
from django.shortcuts import render 

from django.contrib.auth import authenticate ,login,logout 

from django.urls import reverse 

from django.http import JsonResponse 

from app1.forms import  RegisterForm ,LoginForm 

from django.contrib.auth.models import User 

from test2.settings import BASE_DIR 

from django.shortcuts import render ,HttpResponseRedirect 

from app1.models import Profil 

 

 

# Create your views here. 

 

def index(r): 

    ctx={} 

    return render(r,"app/index.html",ctx) 

 

def isconnect(r): 

    if r.user.is_authenticated: 

        return True 

    return False 

 

def register(r): 

    ctx={} 

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

                return render(r,"app/register.html",ctx) 

 

    else: 

        form=RegisterForm() 

 

    ctx['form']=form 

    return render(r,"app/register.html",ctx) 

 

def login_u(r): 

    ctx={ 

        'data':'' 

    }

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

    return render(r,"app/login.html",ctx) 

 

 

 

def logout_user(r): 

    logout(r) 

    return HttpResponseRedirect(reverse('index')) 

 

def view_404(request, *args, **kwargs): 

    return render(request,'app/404.html',{}) 

 

def view_500(request, *args, **kwargs): 

    return render(request,'app/500.html',{}) 

    
