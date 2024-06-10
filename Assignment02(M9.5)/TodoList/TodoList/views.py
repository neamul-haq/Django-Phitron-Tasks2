from django.shortcuts import render
from tasks.models import Tasks

def show_tasks(request):
    data = Tasks.objects.filter(is_completed=False)
    return render(request, 'show_tasks.html', {'data' : data})


def show_complete_tasks(request):
    data = Tasks.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'data' : data})