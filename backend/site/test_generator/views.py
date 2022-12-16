from django.shortcuts import render
from rest_framework.views import APIView
from users.permissions import IsEmailVerifedAndUserAuth
from rest_framework.authentication import TokenAuthentication
from .GenDiffreal import Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, rgr_gen
from .models import Option, Task
from rest_framework.response import Response
from test_generator.serializers import TaskSerializer
from django.core import serializers
from django.http import JsonResponse
from time import time
# Create your views here.

class TestGenerate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEmailVerifedAndUserAuth]

    def post(self, request):
        print(time())
        user = request.user
        task1 = Task1(rgr_gen)
        task3 = Task3(rgr_gen)
        task6 = Task6()
        responce = {}
        option = Option(user=user)
        option.save()
        for tsk in range(len(task1[0])):
            task = Task(option=option, task_number=1, example=task1[0][tsk], answer=task1[1][tsk])
            task.save()
            responce.update({task.id: {'task_number': task.task_number, 'example': task.example, 'answer': task.answer}})
        for tsk in range(len(task3[0])):
            task = Task(option=option, task_number=3, example=task3[0][tsk], answer=task3[1][tsk])
            task.save()
            responce.update({task.id: {'task_number': task.task_number, 'example': task.example, 'answer': task.answer}})
        for tsk in range(len(task6[0])):
            task = Task(option=option, task_number=6, example=task6[0][tsk], answer=task6[1][tsk])
            task.save()
            responce.update({task.id: {'task_number': task.task_number, 'example': task.example, 'answer': task.answer}})
        print(time())
        return Response(responce)


class TestShow(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEmailVerifedAndUserAuth]

    def post(self, request):
        try:
            option = Option.objects.get(user=request.user)
        except:
            return Response({'message': 'Извините для вас тест не сгенерирован!'})
        tasks = TaskSerializer(data=list(Task.objects.all().filter(option=option).values('task_number', 'example', 'answer')), many=True)
        tasks.is_valid()
        return Response({'data' : tasks.validated_data})