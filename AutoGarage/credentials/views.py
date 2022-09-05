from django.contrib import messages, auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['username4']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('booking')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def regis(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if password==cpassword:
         user = User.objects.create_user(username=username,
                                        password=password)
         user.save();
         return redirect("login")
        else:
            print("not matching")

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def booking(request):

    return render(request,"Booking.html")

def form(request):

    return render(request,"Form.html")

def Search(request):
    return HttpResponse()

