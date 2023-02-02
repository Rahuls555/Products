from django.shortcuts import render,redirect,HttpResponse
from . models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request,"home.html")

def AddProduct(request):
    return render(request,"AddProduct.html")

def SaveDetails(request):

    Products=Product()
    Products.name=request.POST['name']
    Products.description=request.POST['description']
    Products.price=request.POST['price']
    Products.save()  
   
    return redirect ("/ProductList")

def ProductList(request):
    listP=Product.objects.all()
    return render(request,"ProductList.html",{'listP':listP})


def RemoveProduct(request,id):
    RemoveP=Product.objects.get(id=id)
    RemoveP.delete()
    return redirect("/ProductList")

def EditProduct(request,id):
    EditP=Product.objects.get(id=id)
    return render(request,"UpdateProduct.html",{'EditP':EditP})

def UpdateProduct(request,id):
    UpdateP=Product.objects.get(id=id)
    UpdateP.name=request.POST['name']
    UpdateP.email=request.POST['email']
    UpdateP.phone=request.POST['phone']
    UpdateP.massage=request.POST['massage']
    UpdateP.save()
    return redirect("ProductList")


def loginhit(request):
    return render(request,"login.html")

def rsignup(request):
    return render(request,"signup.html")


def handleSingup(request):
    if request.method == 'POST':
        username = request.POST['username']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if len(username)>10:
           return redirect("/")
        
        if pass1 != pass2:
            return redirect("/")        

      
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect("/") 
    else:
        return HttpResponse('404 - Not Found')
    
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        
        user= authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully Logged In")
            return redirect('/')
        else:
            return redirect('/')  
    
    else:
      return HttpResponse('404 - Not Found')   
        
def handlelogout(request):
    logout(request)
    return redirect('/')