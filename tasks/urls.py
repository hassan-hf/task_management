from django.urls import path
from .views import TaskListCreateView,TaskRetrieveUpdateView,TaskDeleteView

urlpatterns = [
    path('task/',TaskListCreateView.as_view() , name='task-list-create'),
    path('task/<int:pk>',TaskRetrieveUpdateView.as_view() ,name = 'task-details'),
    path('task/<int:id>/delete/',TaskDeleteView.as_view(),name="task-delete")
    
]
