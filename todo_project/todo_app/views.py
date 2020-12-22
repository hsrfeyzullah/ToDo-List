from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDos
from .forms import ListForm
from django.shortcuts import render

from django.contrib.auth import login, authenticate #1
from django.contrib.auth.forms import UserCreationForm #1
#-----------------------------------
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from functools import wraps
from django.contrib.sessions.models import Session
# Create your views here.

#-------------------------
def index(request):
    user=request.user.id
    if session_verification():
        if request.method == "POST":
            form = ListForm(request.POST or None)
            if form.is_valid:
                form.save()
                todo_list = ToDos.objects.filter(user=user)
                return render(request, "todo_app/index.html",{'todo_list':todo_list})
        else:    
            #todo_list = ToDos.objects.all()       
            todo_list = ToDos.objects.filter(user=user)
            return render(request, "todo_app/index.html",{'todo_list':todo_list})
#--------------------------------------------------------------------------------------------
def about(request):
    return render(request, "todo_app/about.html")      

#--------------------------------------------------------------------------------------------
def create(request):
    print(request.user.id)
    if session_verification():
    #if request.user.is_authenticated:   
        if request.method == "POST":
            form = ListForm(request.POST or None) 
            if form.is_valid:
                post = form.save(commit=False)            
                todo_list = ToDos.objects.all()
                return render(request, "todo_app/create.html",{'todo_list':todo_list})
        else:    
            todo_list = ToDos.objects.all()
            return render(request, "todo_app/create.html",{'todo_list':todo_list})  
    #else:
    #    print("*********************")
    #    return render(request, "accounts/form.html", {'form':form , 'title' : 'Login' })        
#--------------------------------------------------------------------------------------------
def delete(request,ToDos_id):
    if session_verification():
        todo = ToDos.objects.get(pk=ToDos_id)
        todo.delete()
        return redirect("index")
#---------------------------------------------------------------------------------------------
def update(request, ToDos_id):
    if session_verification():
        if request.method == "POST":
            todo_update = ToDos.objects.get(pk=ToDos_id)
            form = ListForm(request.POST or None, instance= todo_update)
            if form.is_valid:
                form.save()
                return redirect("index")
        else:    
            todo_list = ToDos.objects.all()
            return render(request, "todo_app/update.html",{'todo_list':todo_list})  
#--------------------------------------------------------------------------------------------
def yes_finish(request,ToDos_id):
    if session_verification():
        todo = ToDos.objects.get(pk=ToDos_id)
        todo.finished = False   
        todo.save()
        return redirect("index")
#--------------------------------------------------------------------------------------------
def no_finish(request,ToDos_id):
    if session_verification():
        todo = ToDos.objects.get(pk=ToDos_id)
        todo.finished = True
        todo.save()
        return redirect("index") 
#---------------------------------------------------------------------------
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():       
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")      
        user = authenticate(username=username, password=password)
        login(request, user)
        request.session[0]=1  
        return redirect("index")       
    return render(request, "accounts/form.html", {"form":form , 'title' : 'Login' })
#---------------------------------------------------------------------------
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.is_staff = True   #kullanıcı yetkilendirme
        #user.is_superuser = True
        user.save()
        new_user = authenticate(username = user.username, password = user.password)
        login(request, new_user)
        return redirect("create")
    return render(request, "accounts/form.html", {"form":form, 'title' : 'Register' } )
#---------------------------------------------------------------------------
def logout_view(request):
    logout(request)
    return redirect("logout")
#---------------------------------------------------------------------------
def session_verification(request):
    if request.user.is_authenticated:
        return True
    else:
        print("*********************")
        return render(request, "accounts/form.html", {"form":form , 'title' : 'Login' })

#---------------------------------------------------------------------------