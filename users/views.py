from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.contrib import messages
<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
=======
from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User

# from .forms import JoinTeamForm
>>>>>>> cfc3042f8244385880d7418785eff8e7b5ab83e4
# Create your views here.


def home(request):
    client=loveFromClient.objects.all().order_by('-id')
    save=False
    if request.method == "POST":
        Name=request.POST.get('Name')
        email=request.POST.get('email')
        notes=request.POST.get('notes')
        newsletter(name=Name,email=email,specialNotes=notes).save()
        save=True
    feedback = {"clientFeed":client,"message" : save}
    return render(request, 'user/index.html',feedback)


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
    save = False
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Service = request.POST.get('Service')
        Message = request.POST.get('Message')
        requestQuote(Name=Name,Email=Email,SelectedService=Service,Message=Message).save()
        save = True
    return render(request, 'user/quote.html', context={"Quote": save})

def blog(request):
    mainBlog = blogSiteBackend.objects.all().order_by('id')
    blogCntxt = {"blogBackend":mainBlog}
    return render(request, 'user/blogList.html', blogCntxt)


def recentBlog(request):
    if request.method=="GET":
        a=request.GET.get('search')
        if a is not None:
            blogSiteBackend.objects.all().filter(Q(blogRelatedTitle__icontains=a) | Q(writterName__icontains=a) |Q(blogTitle__icontains=a) | Q(blogDetail__icontains=a))
    mainBlog = blogSiteBackend.objects.all().order_by('id')
    blogCntxt = {"blogBackend":mainBlog}
    return render(request, 'user/blog.html', blogCntxt)

def blogDetail(request):
    blogSequence = request.GET.get('msg')
    mainBlog = blogSiteBackend.objects.all().filter(id=blogSequence)
    blogCntxt = {"blogBackend":mainBlog}
    return render(request, 'user/blogDetails.html', blogCntxt)


def features(request):
    return render(request,'user/feature.html')

def order(request):
    item = productItem.objects.all().order_by('-id')
    prdctItem = {"orderItem":item}
    return render(request,'user/orders.html', prdctItem)

def price(request):
    return render(request,'user/price.html')

<<<<<<< HEAD
=======



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


def join_team(request):
    save=False
    if request.method == "POST":
        email_address=request.POST.get('emailAddress')
        full_name=request.POST.get('fullName')
        address=request.POST.get('address')
        phone_number=request.POST.get('phoneNumber')
        gender=request.POST.get('gender')
        colgName=request.POST.get('colgName')
        colgAddress=request.POST.get('colgAddress')
        qualification=request.POST.get('qualification')
        spendTime=request.POST.get('spendTime')
        availablityTime=request.POST.get('availablityTime')
        internshipdate=request.POST.get('internshipdate')
        internshiparea=request.POST.get('internshiparea')
        desktopornot=request.POST.get('desktopornot')
        internshippurpose=request.POST.get('internshippurpose')
        anysuggestion=request.POST.get('anysuggestion')
        JoinTeam(email_address=email_address,full_name=full_name,address=address,phone_number=phone_number,gender=gender,colg_name=colgName,colg_address=colgAddress,qualification=qualification,spend_time=spendTime,availablity_time=availablityTime,internship_date=internshipdate,internship_area=internshiparea,desktop_or_not=desktopornot,internship_type=internshippurpose,any_suggestion=anysuggestion).save()
        save=True
    context = {"message2" : save}
    return render(request, 'user/index.html',context)
>>>>>>> cfc3042f8244385880d7418785eff8e7b5ab83e4
