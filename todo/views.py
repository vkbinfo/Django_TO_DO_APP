from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .todoForm import TodoForm, NewToDoForm
# Create your views here.


def index(request):
    todo_list = Todo.objects.all()
    # normal form
    # form = TodoForm()

    # model(table) class based form, Which is better from above TodoForm
    modeltodoform = NewToDoForm()
    context = {'todo_list': todo_list, 'form': modeltodoform}
    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    # processing in normal form class
    # formData = TodoForm(request.POST)
    # if formData.is_valid():
    #     new_todo = Todo(text=formData.cleaned_data['text_input'])
    #     new_todo.save()

    # let's use our model based class form to
    class_form_data = NewToDoForm(request.POST)
    # if we can give instance of a model object, as second argument in above line, that we can update that instance.
    # isn't it awesome.
    if class_form_data.is_valid():
        # because our class_form_data has already referencd model through form, we can just directly save that
        class_form_data.save()
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
