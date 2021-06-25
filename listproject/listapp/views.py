from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import Taskform
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
class Detailtaskview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class Updatetask(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbdetailview',kwargs={'pk':self.object.id})
class Deletetask(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbview')

# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request, 'home.html',{'task':task1})
# def detail(request):
#     task=Task.objects.all()
#     return render(request,'detail.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id=id)
    f = Taskform(request.POST or None ,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'f':f})