from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .todoForm import TodoForm
# Create your views here.


def index(request):
    todo_list = Todo.objects.all()
    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    formData = TodoForm(request.POST)
    if formData.is_valid():
        new_todo = Todo(text=formData.cleaned_data['text_input'])
        new_todo.save()
    return redirect('index')


def complete_todo(request, todo_id):
    todo_item = Todo.objects.get(pk=todo_id)
    todo_item.complete = True
    todo_item.save()
    return redirect('index')


def delete_completed_todos(request):
    Todo.objects.filter(complete__exact = True).delete()
    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')
