from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from adminapp.models import*
from django.contrib.auth import logout




# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':

        nm=request.POST.get('name')
        ad=request.POST.get('address')
        em=request.POST.get('email')
        phno=request.POST.get('phone')
        use=request.POST.get('username')
        pa=request.POST.get('password')
        obj1=login()
        obj1.username=use
        obj1.password=pa
        obj1.role="client"
        obj1.save()
        ob=register()
        ob.name=nm
        ob.address=ad
        ob.phono=phno
        ob.email=em
        ob.password=pa
        ob.username=use
        ob.log=obj1
        ob.save()

        return HttpResponse("INSERTED")
    else:
        return render(request,'registration.html')

def signin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pas=request.POST.get("password")
        if login.objects.filter(username=un,password=pas).exists():
            obj=login.objects.filter(username=un,password=pas)
            for i in obj:
                r=i.role
                lid=i.id
                request.session['sid']=lid
                if r=='client':
                    reg=register.objects.get(log_id=lid)#registration page forienkey field  log_id
                    obj2=products.objects.all()
                    name=reg.name
                    return render(request,"clientlogin.html",{'name':name,"obj2":obj2})

                else:
                    return HttpResponse("ERROR")
        else:
                    error="invalid login data"
                    return render(request,"login.html",{'error':error})
    else:
        return render(request,"login.html")


def client(request):
    return render(request,"clientlogin.html")

def vegetables(request):
    obj=products.objects.all()
    return render(request,"vegetables.html",{"obj":obj})

def cart(request,id):
     p=products.objects.get(id=id)
     return render(request, "cart.html", {"p": p})

def remove(request,id):

    ord = orders1.objects.get(id=id)
    ord.delete()
    return vegetables(request)

def orde(request,id):
    p = products.objects.get(id=id)
    nm=p.name
    w=p.price
    loginid=request.session['sid']
    reg=register.objects.get(log_id=loginid)
    if request.method=="POST":
        q=request.POST.get('number')
        c=int(q)*int(w)
        obj=orders1()
        obj.product=nm
        obj.quantity=q
        obj.img=p.img
        obj.pri=c
        obj.user=reg.name
        obj.uid=reg
        obj.pid=p
        obj.save()
        return order(request)
    else:
      return render(request,"cart.html",{"p":p})

def order(request):
    loginid = request.session['sid']
    ord = orders1.objects.filter(uid_id=loginid)
    p=[]
    for i in ord:
        prod=products.objects.get(id=i.pid_id)
        p.append(prod)
    suma=[]
    for j in ord:
        suma.append(j.pri)
    c=(sum(suma))

    return  render(request,"orders.html",{"ord":ord,'p':p,'c':c,})

def payment(request):
    loginid = request.session['sid']
    ord = orders1.objects.filter(uid_id=loginid)
    suma = []
    for j in ord:
        suma.append(j.pri)
    c = (sum(suma))

    return  render(request,"payment.html",{'c':c})


def pay(request):
 if request.method=="POST":
    loginid = request.session['sid']
    reg=register.objects.get(log_id=loginid)


    o = orders1.objects.filter(uid_id=loginid)




    for i in o:
       m=i.img
       c= i.product
       u=i.user
       pr=i.pri
       q=i.quantity
       ui=i.uid
       p=i.pid
       obj = orders3()
       obj.product = c
       obj.quantity = q
       obj.img=m
       obj.pri = pr
       obj.user = u
       obj.uid = ui
       obj.pid = p
       obj.save()
    o.delete()
    ob = paym()
    nm = request.POST.get('cardname')
    num = request.POST.get('cardnumber')
    t = request.POST.get('total')


    ob.cardname = nm
    ob.cardnumber = num
    ob.subtotal = t
    ob.uid = reg


    ob.save()

    return HttpResponse("order placed")
 return render(request,"clientlogin.html")

def myorders(request):
    loginid = request.session['sid']
    o = orders3.objects.filter(uid_id=loginid)
    return render(request,"myorders.html",{'o':o})

def mycarts(request):
    loginid = request.session['sid']
    o = orders1.objects.filter(uid_id=loginid)
    return render(request,"myorders.html",{'o':o})




def log(request):
    if request.method=="POST":
        logout(request)
        return redirect('/')
