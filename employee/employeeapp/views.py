from django.shortcuts import render
from .forms import MyForm
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect


@login_required
def home(request):
    return render(request,"home.html")
# def show(request):
#      if request.method == 'POST':
#          form = MyForm(request.POST)
#          if form.is_valid():
#              id = form.cleaned_data['id']
#              name = form.cleaned_data['name']
#              age= form.cleaned_data['age']
#              department = form.cleaned_data['department']
#              return render(request, "show.html", {'id': id, 'name':name, 'age':age, 'department':department})       
#      else:
#             form = MyForm()
#             return render(request,"home.html", {'form':form})     


def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username= uname,password = pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"invalid login"})
    

def logout_view(request):
    logout(request)
    return redirect('login')


def sign_up(request):
    try:
        form =UserCreationForm(request.POST)
        if request.method =="POST":
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            return render(request,'sign_up.html',{'form': userform,'msg':"Invalid login"})
    except Exception as e:
        print(e)
        userform = UserCreationForm()
        return render(request,'sign_up.html',{'form':userform})
                



@login_required
def addEmployee(request):
    Name = request.POST['name']
    Address = request.POST['address']
    Age = request.POST['age']
    empobj = Employee(name= Name, address = Address, age = Age)
    empobj.save()
    return render(request, "home.html",{"msg":"Employee added"})
@login_required
def display(request):
    empdtls = Employee.objects.all()
    return render(request,"home.html",{'emp':empdtls})
@login_required
def deleteEmployee(request):
    empname = request.POST['name']
    empdtls = Employee.objects.filter(name=empname)
    empdtls.delete()
    return render (request,'home.html',{"msg":"Deleted"})
@login_required
def updatename(request):
    try:
        oldname = request.POST["oldname"]
        newname = request.POST["newname"]
        emp = Employee.objects.filter(name = oldname)
        if emp.exists():
            emp.update(name = newname)
            return render(request,"home.html",{'msg1':"updated"})
        else:
            return render(request,"home.html",{'msg1':"no record found"})
    except Exception as e:
        print(e)
        return render(request, "home.html",{'msg1':"Not updated"})