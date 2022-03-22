from dataclasses import dataclass
from django.shortcuts import redirect, render
from app.forms import AgenteForm
from app.models import Agente


# Create your views here.

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Agente.objects.filter(Função__icontains=search)
    else:
        data['db'] = Agente.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = AgenteForm()
    return render(request, 'form.html', data)


def create(request):
    form = AgenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Agente.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Agente.objects.get(pk=pk)
    data['form'] = AgenteForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Agente.objects.get(pk=pk)
    form = AgenteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Agente.objects.get(pk=pk)
    db.delete()
    return redirect('home')
