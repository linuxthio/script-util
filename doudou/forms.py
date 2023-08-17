
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




