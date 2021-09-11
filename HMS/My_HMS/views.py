from django.shortcuts import render,HttpResponseRedirect , redirect
#from .forms import PatientRegistration
from .models import Patient1 as Patient
from django.contrib import messages

# Create your views here.

def index(request):
    """
    THis function will add records to the database.
    """
    Pat=Patient.objects.all()
    if request.method=="POST":
        pname = request.POST.get("Name")
        page = request.POST.get("Age")
        padd = request.POST.get("Address")
        pcity = request.POST.get("City")
        pdise = request.POST.get("Disease")
        #fm=PatientRegistration(request.POST)
        req=Patient.objects.filter(Name=pname)
        reg=Patient(Name=pname,Age=page,Address=padd,Disease=pdise,City=pcity)
        if(req.count() == 1):
            messages.warning(request,"Given Name is Already Exist")
            return render(request,'insertdisplay.html',{'Patient':Pat,'pdata':reg})
        elif(req.count()==0):
            reg.save()
            messages.success(request, 'Form Submitted!',extra_tags='alert')
            return redirect('/')
        else:
            messages.warning(request, 'Please Fill-up Correct Details')
             
    return render(request,'insertdisplay.html',{'Patient':Pat})

# This Fuction will Delete Records

def delete_data(request,Pid):
    req=Patient.objects.filter(PID=Pid)
    if(req.count() == 1):
        if request.method=="GET":
            req.delete()
            return redirect('/')
    else:
            return render(request,'error.html')

def update_data(request,Pid):
    req=Patient.objects.filter(PID=Pid)
    if(req.count() == 1):
        req=Patient.objects.get(PID=Pid)
        if request.method =="GET":
            Pat=Patient.objects.all()
            return render(request,'updatepatient.html' ,{'data':req,'Patient':Pat,'current':Pid})

        elif request.method == "POST":
            req.Name = request.POST.get("Name")
            req.Age = request.POST.get("Age")
            req.Address = request.POST.get("Address")
            req.City = request.POST.get("City")
            req.Disease = request.POST.get("Disease")
            req.save()
            return redirect('/')
    else:
        return render(request,'error.html')
