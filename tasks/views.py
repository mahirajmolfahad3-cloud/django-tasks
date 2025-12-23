from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class Form(forms.Form):
    task = forms.CharField(label="New Task")

def index(requests):
    if "tasks" not in requests.session:
        requests.session["tasks"] = []
    return render(requests, "tasks/index.html", {
        "tasks": requests.session["tasks"]
    })

def add(requests):
    if "tasks" not in requests.session:
        requests.session["tasks"] = []
    if requests.method == "POST":
        task = Form(requests.POST)
        if task.is_valid():
            x = task.cleaned_data["task"]
            requests.session["tasks"] += [x]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(requests, "tasks/add.html", {
                "form": task
            })
    return render(requests, "tasks/add.html", {
        "form": Form()
    })