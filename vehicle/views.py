from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import vehicles
# Create your views here.
def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        a=request.POST.get('username')
        b=request.POST.get('password')
        c=request.POST.get('email')
        User.objects.create_user(username=a,password=b,email=c)
        return redirect('vehicle:login')


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        a=request.POST.get('uname')
        b=request.POST.get('psw') 
        ob=authenticate(username=a,password=b)
        if ob is not None:
            if a=='admin':
                return redirect ('vehicle:details')
            else:
                return redirect('vehicle:vehicledetails')
        else:
            return render(request,'login.html')


    
        
def home(request):
    return render(request,'home.html')

def details(request):
    ob=vehicles.objects.all()
    return render(request,'details.html',{'obj':ob})



def vehicledetails(request):
    ob=vehicles.objects.all()
    return render(request,'vehicledetails.html',{'obj':ob})


def update(request,pk):
    if request.method=='GET':
        ob=vehicles.objects.get(id=pk)
        return render(request,'update.html',{'ob':ob})
    else:
        a=request.POST.get('no')
        b=request.POST.get('type')
        c=request.POST.get('model')
        d=request.POST.get('discription')

        vehicles.objects.filter(id=pk).update(vehicle_no=a,vechicle_type=b,vechicle_model=c,discription=d)
        return redirect ('vehicle:details')
