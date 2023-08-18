from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.


def ff(r):
    form = DFo
    if r.method == 'POST':
        form = DFo(r.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('model')
    return render(r, 'form.html', {'form': form})


def mf(r):
    form = DM.objects.all()
    return render(r, 'model.html', {'form': form})
