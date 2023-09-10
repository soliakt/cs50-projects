from django.shortcuts import render
from django import forms

from . import util

class NewEntryForm(forms.Form):
    task = forms.CharField(label="New Entry")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    return render(request, "encyclopedia/add.html",{
        "form": NewEntryForm()
    })