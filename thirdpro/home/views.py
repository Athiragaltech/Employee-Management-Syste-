from django.shortcuts import render,redirect
from . models import employee

# def index(request):
#     return render(request,'index.html')

def index(request):
    data ={
        'emp' :employee.objects.all()

    }
    print(data)
    return render(request,'index.html',data)
def edit1(request):
    data ={
        'emp' :employee.objects.all()

    }
    print(data)
    return render(request,'contact.html',data)
def add(request):
    return render(request,'about.html')
def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        place=request.POST.get('place')
        desig=request.POST.get('desig')
        country=request.POST.get('country')
        mobile=request.POST.get('mobile')
       

        query=employee(name=name,age=age,place=place,desig=desig,country=country,mobile=mobile)
        query.save()
    return  redirect("/")
def delete(request,id):
    dlt=employee.objects.get(id=id)
    dlt.delete()
    return redirect("/")
def edit(request):
    data={"data":employee.objects.all()}
    return render(request,'edit.html',data)
def update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        place=request.POST.get('place')
        desig=request.POST.get('desig')
        country=request.POST.get('country')
        mobile=request.POST.get('mobile')
       
        edit=employee.objects.get(id=id)
        edit.name=name
        edit.age=age
        edit.place=place
        edit.desig=desig
        edit.country=country
        edit.mobile=mobile
      
        edit.save()
        return redirect("/")
    
    
def edit2(request,id):
    data ={
        'emp' :employee.objects.get(id=id)

    }
    print(data)
    return render(request,'update.html',data)
