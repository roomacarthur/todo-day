from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),  # List all tasks
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),  # View task details
    path('create/', TodoCreateView.as_view(), name='todo-create'),  # Create a new task
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),  # Update a task
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),  # Delete a task
]