from django.shortcuts import render, redirect
from django.views.generic import View

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Task
from .forms import TaskForm

class TaskView(View):
    def get(self, request):
        tasks = list(Task.objects.values())

        if request.is_ajax():
            return JsonResponse({'tasks': tasks}, status=200)

        return render(request, 'task.html')

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            new = form.save()
            return JsonResponse({'task': model_to_dict(new)}, status=200)

        return redirect('task_view')
