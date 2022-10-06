from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['mail']
        # phone = request.POST['phone']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            #checking password is matching
            if User.objects.filter(username=username).exists():
                #checking username is existing or not
                messages.info(request, 'User name is already exists !')
                # messagebox.showerror('exist user', 'user name already exist')
                return redirect('register')
            #if user name is existing page will be reloaded and wait for new entry
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is already exists')
                return redirect('register')
            else:
                #create user on database User is keyword, user is variable
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save();
                #new user saved
                return redirect('login')

        else:
            return messages.info(request, 'Password is not matching !')
            #else part for password matching
            return redirect('register')
        return redirect('/')
    #user created successfully and go to the home page of the website
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')