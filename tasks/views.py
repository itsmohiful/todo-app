from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Tasks

# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request,"tasks/index.html",context)


def add_task(request):
    tasks = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')

        # else:
        #     form = TaskForm()

    context = {
        'tasks' : tasks
    }

    return render(request,'tasks/add_task.html',context)


def edit_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task_form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    context = {
        'task_form' : task_form
    }

    return render(request,'tasks/task_edit.html',context)



def task_view(request,pk):
    task = get_object_or_404(Tasks, pk=pk)
    context = {
        'task' : task
    }
    return render(request,"tasks/task_view.html",context)


def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('tasks:index')

    context = {
        'task' : task
    }
    return render(request,'tasks/task_delete.html',context)


def complete(request):
    task = Tasks.objects.filter(is_complete=True)
    context = {
        'tasks' : task
    }
    return render(request,'tasks/complete.html',context)


def incomplete(request):
    task = Tasks.objects.filter(is_complete=False)
    context = {
        'tasks' : task
    }
    return render(request,'tasks/incomplete.html',context)
