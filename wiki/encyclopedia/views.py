from xml.dom import ValidationErr
from .util import get_entry, render_markdown_to_html
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django import forms
from django.http import Http404
from .util import get_entry 

from . import util

entries = []
class NewEntryForm(forms.Form):
    entry = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Esto crea una vista separada para la página 404. 
def error_404(request):
    return render(request, "encyclopedia/404.html")


def content_page(request, entry_title):
    content = get_entry(entry_title)
    if content is None:
        raise Http404("Entry not found")
    
    return render(request, "encyclopedia/contentPage.html", {
        "title": entry_title,
        "content": content,
    })

def add(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entry"]
            content = form.cleaned_data["content"]
            try: 
                util.save_entry(entry, content)
                # Esto guarda la entrada utilizando la función save_entry de util
                return redirect("encyclopedia:index")
            except ValidationError as e:
                return redirect("encyclopedia:404")
        else:
            return redirect("encyclopedia:404")
    return render(request, "encyclopedia/add.html",{
        "form": NewEntryForm()
    })

def view_entry(request, entry_title):
    content = get_entry(entry_title)
    if content is None:
        raise Http404("Entry not found")
    
    html_content = render_markdown_to_html(content)

    return render(request, "encyclopedia/contentPage.html", {
        "title": entry_title,
        "content": html_content,
    })
