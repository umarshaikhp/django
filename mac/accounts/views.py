from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def register(request):
    if request.method == 'POST':
                # first_name = request.POST['first_name']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                username = request.POST['username']
                password1 = request.POST['password']
                password2 = request.POST['password1']
                email = request.POST['email']
            

                if password1==password2:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, "username taken")
                        return redirect('register')
                    elif User.objects.filter(email=email).exists():     
                        messages.info(request, "email taken")
                        return redirect('register')

                    else:     
                        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name )
                        user.save()
                        print("user created")
                        return redirect('login')

                else: 
                    messages.info(request, 'password is not matched')  
                    return redirect('register')

    else :
        return render(request,'register.html')


def login(request):
    print("umar shaikh")

    if request.method == 'POST':
        user1 = request.POST['username']
        pass1 = request.POST['password']

        # print(user1,pass1)
        # user2 = User.objects.filter(username=user1)
        # auth object method autheticated that is used to check the user is authenticated or not 
        # if user is autheticated then it will return user object otherwise it will return None
        user = auth.authenticate(request,username=user1,password=pass1)
        print(user)

        print("authenticate time",user)
        # print("filter time",user2)    

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")  
            return redirect('login')
    else : 
        print("hii")   
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
