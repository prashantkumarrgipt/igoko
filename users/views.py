from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
# Create your views here.


def home(request):
  
    return render(request, 'user/index.html')


def about(request):
    return render(request, 'user/aboutus.html')


def services(request):
    client=loveFromClient.objects.all().order_by('-id')
    feedback = {"clientFeed":client}
    return render(request, 'user/services.html',feedback)


def contact(request):
    save=False
    if request.method == "POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Subject=request.POST.get('subject')
        Message=request.POST.get('message')
        contactus(name=Name,subject=Subject,email=Email,message=Message).save()
        save=True
    return render(request, 'user/contactus.html', context={"message" : save})

def quote(request):
    return render(request, 'user/quote.html')

def blog(request):
    return render(request, 'user/blog.html')

def features(request):
    return render(request,'user/feature.html')

def order(request):
    return render(request,'user/orders.html')

def price(request):
    return render(request,'user/price.html')
# signup
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<5:
            messages.error(request, " Your user name must be under 5 characters")
            return redirect('home')

        # username must be only letters and numbers 
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        # password should match 
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect(request.META.get('HTTP_REFERER', 'home'))

    else:
        return HttpResponse("404 - Not found")

# login
def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

# logout
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(request.META.get('HTTP_REFERER', 'home'))