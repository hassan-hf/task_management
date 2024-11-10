from rest_framework import generics,status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class TaskDeleteView(generics.DestroyAPIView):
    queryset =Task.objects.all()
    serializer_class = TaskSerializer
    
    def delete(self,request , *args , **kwargs):
        try:
            task =self.get_object()
            task.delete()
            return Response({"message":"Task Deleted successfuuly"},status=status.HTTP_204_NO_CONTENT)            
        except Task.DoesNotExist:
            return Response({"error":"Task not found"},status=status.HTTP_404_NOT_FOUND)
        

