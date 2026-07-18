from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskShortSerializer, TaskFullSerializer

class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskShortSerializer
        return TaskFullSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskFullSerializer
