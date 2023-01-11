from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    list = Todo.objects.all()

    if request.method == 'POST':
        new_todo = Todo( title = request.POST['title'] )
        new_todo.save()
        return redirect('/')
    return render(request,'index.html', {'todo': list})

def delete(request, pk):
    delete_todo = Todo.objects.get(id = pk)
    delete_todo.delete()
    return redirect('/')
    
    