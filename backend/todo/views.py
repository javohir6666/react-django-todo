from rest_framework import viewsets
from .serialiers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
