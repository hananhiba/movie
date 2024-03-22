from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['confirm_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('credentials:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exist")
                return redirect('credentials:signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
                print("user created")
                messages.success(request, "Welcome user")
                return redirect('credentials:login')
        else:
            messages.info(request, "Password not matching")
            return redirect('credentials:signup')
    return render(request, "signup.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('credentials:login')
    return render(request, "login.html")


def userview(request, user_id):
    view = User.objects.get(id=user_id)
    return render(request, "ViewUser.html", {'view': view})


def logout(request):
    auth.logout(request)
    return redirect('/')
