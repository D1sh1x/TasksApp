from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm

def index(request):
    tasks = Tasks.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Задачник', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не корректна'
    form = TasksForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


