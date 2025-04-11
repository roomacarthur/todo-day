from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm

# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(category__isnull=False).order_by('-created_at')

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todos/todo_detail.html'
    context_object_name = 'todo'

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo-list')

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todos/todo_form.html'
    fields = ['title', 'description', 'is_completed', 'category']
    success_url = reverse_lazy('todo-list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list')
