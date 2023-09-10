from django.shortcuts import render, redirect
from django import forms

from . import util

entries = []
class NewEntryForm(forms.Form):
    entry = forms.CharField(label="New Entry")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
           entry = form.cleaned_data["entry"] 
           # Esto guarda la entrada utilizando la función save_entry de util
           util.save_entry(entry, "")
           return redirect("encyclopedia/index.html")
        else:
            return render(request, "encyclopedia/add.html",{
                "form": form
            })
    return render(request, "encyclopedia/add.html",{
        "form": NewEntryForm()
    })