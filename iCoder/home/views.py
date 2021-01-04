from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'home/home.html') 

def about(request): 
    return render(request, 'home/about.html') 

def contact(request): 
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<2 or len(phone)<10:
            messages.error(request,'Please fill the form correctly.')
        else:    
            contact_obj=Contact(name=name,email=email,phone=phone,content=content)
            contact_obj.save()
            messages.success(request,'your problem has been sent')
    return render(request, 'home/contact.html') 

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPost=[]
    else:    
         allPost= Post.objects.filter(title__icontains=query)
    params={'allpost':allPost,'query':query}
    return render(request,"home/search.html",params)

def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request,"Username should not be more than 10 characters, please fill again")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request,"please match the passwords again")
            return redirect('home')  
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account has been created")
        return redirect('home')
    else:
        return HttpResponse('404-not found')  

def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('home')
            
        else:
            messages.error(request,"Invalid credentials")    
            return redirect('home')
    return HttpResponse('404-not found')        

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('home')