from django.contrib.auth import get_user_model
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer

from ..models import Task


User = get_user_model()


class TaskView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').replace("Bearer ", "")
        user_id=jwt.decode(jwt=token, key='django-insecure-5e77^plgzw#p^00%3ece8l9nna)v!2%5wz=%w^x)t2h%20h2tr',
                         algorithms=['HS256'])['user_id']
        tasks = Task.objects.filter(user__id=user_id)
        serialized = TaskSerializer(tasks, many=True)
        return Response(serialized.data)


class AddTaskView(APIView):
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').replace("Bearer ", "")
        user_id=jwt.decode(jwt=token, key='django-insecure-5e77^plgzw#p^00%3ece8l9nna)v!2%5wz=%w^x)t2h%20h2tr',
                         algorithms=['HS256'])['user_id']
        request.data["user"] = user_id
        serialized = TaskSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
        print(serialized.errors)
        return Response({"message": "success"})