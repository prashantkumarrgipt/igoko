from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
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

