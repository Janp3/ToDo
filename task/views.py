
from datetime import date

from django.shortcuts import render

from task.models import task

# Create your views here.

start_date = date.today()


def create_task(request):

    if request.method == 'GET':
        return render(request, 'task/pages/create.html')
    else:
        title = request.POST.get('title')
        date_form = request.POST.get('date')
        add = task.objects.create(title=title, date=date_form)
        add.save()
        return render(request, 'task/pages/create.html', context={
            'date': start_date
        })


def update_task(request, id):
    task_info = task.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'task/pages/update.html', context={
            'task': task_info,
            'date': start_date,
        })

    # else:


def home(request):
    task_ = task.objects.all().order_by('-id')
    context = {
        'task': task_
    }
    return render(request, 'task/pages/home.html', context=context)


def delete_task(request, id):
    if request.method == 'GET':
        return render(request, 'task/pages/delete.html')

    else:
        task_ = task.objects.all().order_by('-id')
        context = {
            'task': task_
        }
        deleting = task.objects.get(pk=id)

        deleting.delete()
        return render(request, 'task/pages/home.html', context=context)
