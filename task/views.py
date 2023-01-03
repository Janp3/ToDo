
from django.shortcuts import render

from task.models import task

# Create your views here.


def create_task(request):

    if request.method == 'GET':
        return render(request, 'task/pages/create.html')
    else:
        title = request.POST.get('title')
        date_form = request.POST.get('date')
        add = task.objects.create(title=title, date=date_form)
        add.save()
        return render(request, 'task/pages/create.html')


def update_task(request):
    return render(request, 'task/pages/update.html')


def home(request):
    task_ = task.objects.all().order_by('-title')
    context = {
        'task': task_
    }
    return render(request, 'task/pages/home.html', context=context)
