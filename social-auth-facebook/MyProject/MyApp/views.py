from django.shortcuts import render

# Create your views here.


import MyProject
from django.shortcuts import render
from django.contrib.auth import authenticate , login
from . form import LoginForm
from django.http import HttpResponse

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])    
        
            if user is not None:
                login(request, user)
                return HttpResponse('authentication was successfull')

            else:
                return HttpResponse('authentication was failed')

    else:
        form = LoginForm()
        
        
        
    return render(request, 'login.html',{'form':form})

