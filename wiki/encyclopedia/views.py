from django.shortcuts import render, redirect
from django import forms
from . import util
import markdown2
import random


class EntryForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(label="Content", widget=forms.Textarea)



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title): 
    page = util.get_entry(title)
    if page is not None:
        content = markdown2.markdown(page)
    else:
        content = '<h1>page Not found<h1/>'

    return render(request, "encyclopedia/entry.html",{"title": title, "entry": content})



def create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if title in util.list_entries():
                return render(request, "encyclopedia/create.html", {"form": form, "error": "Title already exists"})
            util.save_entry(title, content)
            return redirect('entry', title=title)
    else:
        form = EntryForm()
    return render(request, "encyclopedia/create.html", {"form": form, "error": None})



def edit(request, title):
   
    content = util.get_entry(title.strip())
    if content is None:
        return render(request, "encyclopedia/edit.html", {'error': "no such page"})
    if request.method == "GET":
        content = request.GET.get("content").strip()
        if content == "" or content is None:
            return render(request, "encyclopedia/edit.html",
                          {"message": "no content", "title": title, "content": content})
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})



def randomPage(request):
    pages = util.list_entries()
    randmPage = random.choice(pages)
    return redirect('entry', title=randmPage)   



def search(req):
    query = req.POST.get('q', '').lower()  
    if not query:
        return render(req, "encyclopedia/search.html", {"error": "Please enter a search term."})

    query_pages = []
    for entry in util.list_entries():
        if query in entry.lower():  
            query_pages.append(entry)
        
    return render(req, "encyclopedia/search.html", {"entries": query_pages, "q": query})

#make the video views functions and html done //