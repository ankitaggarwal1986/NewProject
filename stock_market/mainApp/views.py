from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Stocks
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

#Home Page
def home(request):
    return render(request, "index.html")    

#Add Page
def add(request):

    if request.method == "POST":
        s=Stocks()
        s.name=request.POST.get("name")
        s.ticker=request.POST.get("ticker")
        s.stock_exchange=request.POST.get("stock_exchange")
        s.price=request.POST.get("price")
        s.slug =request.POST.get("name").replace(" ","-")
        s.save()
        return HttpResponseRedirect("listing")
    return render(request, "add.html")   

#Edit Page
def edit(request, id):
    
    data=Stocks.objects.get(id=id)

    if request.method=="POST":
        data.name=request.POST.get("name")
        data.ticker=request.POST.get("ticker")
        data.price=request.POST.get("price")
        data.save()
        return redirect("listing")
    elif request.method=="GET":
        return render(request, "edit.html",{"Data": data}) 

#Delete Page
def delete(request,id):
    data=Stocks.objects.get(id=id)
    data.delete()
    return redirect("listing")   

#Details Page
def detail(request,slug):
    data=Stocks.objects.get(slug=slug)
    return render(request, "detail.html",{"Data":data})         

#Listing Page
def listing(request):

    data=Stocks.objects.all()
    return render(request, "listing_page.html",{"Data": data})        
     
#Sign Up Page
def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registerd!")
            return redirect('home')  

        if len(username)>10:
            messages.error(request,"Username must not be more than 10 characters!")
            

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            

        if not username.isalnum():
            messages.error(request, "Username should me Alpha-numeric!")
            return redirect('home')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request,"Your Account has been successfully created!")
        return redirect('listing')

    return render(request, "signup.html")

#Sign In Page
def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return redirect("listing")
        else:
            messages.error(request, "Bad Credentials!")
            return redirect("signin")    

    return render(request, "signin.html")  

#Sign Out Page
def signout(request):
    logout(request)
    messages.success(request,"You have successfully logged out!") 
    return redirect("/")     
