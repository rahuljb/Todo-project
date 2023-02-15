from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Create your views here.

# class TaskListView(ListView):
#     model = Task
#     template_name = 'listview.html'
#     context_object_name = 'tasK1'
#     success_url = reverse_lazy('cbvhome')
#
#
# class TaskDetailView(DetailView):
#     model = Task
#     template_name = 'details.html'
#     context_object_name = 'tas'
#
#
# class TaskUpdateView(UpdateView):
#     model = Task
#     template_name = 'update.html'
#     context_object_name = 'tas'
#     fields = ('name', 'priority', 'date')
#
#     def get_success_url(self):
#         return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})
#
#
# class TaskDeleteView(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('cbvhome')


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'tas': task1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'forms': form, 'task': task})
