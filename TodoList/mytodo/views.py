from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from mytodo.models import Todo
# Create your views here.

def index(request):
    todos=Todo.objects.all()
    template=loader.get_template('mytodo/index.html')
    context={'todos':todos}
    return HttpResponse(template.render(context,request))

def write(request):
    newtodo = request.POST['newtodo']
    Todo.objects.create(contents=newtodo)
    return redirect('todolist:index')

def delete(request, todo_id):
    foundtodo = get_object_or_404(Todo, pk=todo_id)
    foundtodo.delete()
    return redirect('todolist:index')
