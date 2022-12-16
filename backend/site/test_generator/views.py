from django.shortcuts import render
from rest_framework.views import APIView
from users.permissions import IsEmailVerifedAndUserAuth
from rest_framework.authentication import TokenAuthentication
from .GenDiffreal import Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, rgr_gen
from .models import Option, Task
from rest_framework.response import Response
# Create your views here.

class TestGenerator(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEmailVerifedAndUserAuth]

    def post(self, request):
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
        return Response(responce)
        
