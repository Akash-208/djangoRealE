from django.shortcuts import render,HttpResponse,redirect
from myapp.models import realestate
from . models import realestate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout,login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def details(request):
    user = request.user
    type = request.POST.get('type')
    address = request.POST.get('address')
    price = request.POST.get('price')
    numofbd = request.POST.get('numofbedrooms')
    numofbth = request.POST.get('numofbathrooms')
    area = request.POST.get('area')
    mail = request.POST.get('mail')
    image = request.FILES.get('files')

    realestate(user = user,  title=type,mail=mail,address=address,area=area,numofbedroom=numofbd,numofbathrooms=numofbth,price=price,picture=image).save()
    return redirect('home')

    
def list(request):
    items = realestate.objects.all()
    return render(request,'listed.html',{'dict':items})

def loginpage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
                    
            user = authenticate(username = username, password = password)
            if user is None:
                messages.error(request,'Invalid password')
                return redirect('loginpage')
            else:
                login(request, user)
                return redirect('home')
        return render(request,'login.html')

    

def registerpage(request):
    if request.method=="POST":
        fullname = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('registerpage')

        user = User.objects.create(
            first_name = fullname,
            username = username,
        )
        user.set_password(password)
        user.save()
        return redirect('loginpage')
    return render(request,'register.html')

def userposts(request):
    post = realestate.objects.filter(user=request.user)
    return render(request,'userpost.html',{'p':post})

def remove(request,id):
    post = realestate.objects.get(id = id)
    post.delete()
    return redirect('userpost')


def logoutview(request):
    logout(request)
    return redirect('loginpage')
