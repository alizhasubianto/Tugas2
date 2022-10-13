from django.shortcuts import render
from todolist.forms import Input_Form
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/todolist/login')
def show_todolist(request):
    getToDoList = Task.objects.filter(user=request.user)
    context = {
        'username': request.user,
        'to_do_list' : getToDoList,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task(request):
    form = Input_Form()

    if request.method == "POST":
        form = Input_Form(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Task telah berhasil dibuat!')
            return redirect('todolist:show_todolist')

    context = {'form': form}
    return render(request, 'createtask.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
@csrf_exempt
def status(request, id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete(request, id):
    delete = Task.objects.get(pk=id)
    delete.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
@csrf_exempt
def show_json_by_id(request):
    data = Task.objects.filter(user=request.user).order_by('id')
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_ajax(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        description = request.POST['description']
        task_item = Task.objects.create(
            user=user, 
            title=title, 
            description=description
        )
        task_item.save()
        return JsonResponse({"instance": "Task successfully added!"}, status=200)


        

# Create your views here.
