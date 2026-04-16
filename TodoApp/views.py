from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwner
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from .pagination import TaskPagination

# CRUD Start 

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = TaskPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
# class TestAuth(APIView):
#     def get(self, request):
#         username = request.header.get("username")

#         if username == "Ahmad":
#             return Response({"message" : "Authenticated"})
        
#         return Response({"message" : "Login here"})

# class TaskList(ListCreateAPIView):
#      queryset = Task.objects.all()
#      serializer_class = TaskSerializer



# class TaskList(APIView):
#     def get(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TaskDetails(RetrieveUpdateDestroyAPIView):
#      queryset = Task.objects.all()
#      serializer_class = TaskSerializer
# class TaskDetails(APIView):

#     def get_objects(self, request, pk):
#         try:
#             current_task = Task.objects.get(pk=pk)
#         except current_task.DoesNotExist:
#             raise Http404
        

#     def put(self, request, pk):
            
#             task = self.get_objects(pk)
#             serializer = TaskSerializer(task, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#             task = self.get_objects(pk)
#             task.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
