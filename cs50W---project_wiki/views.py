from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util

import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    page = util.get_entry(title)
    if page is not None:
        content = markdown(page)
    else:
        content = '<h1>page Not found<h1/>'

    return render(request, "encyclopedia/entry.html",{"title": title, "entry": content})


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title').strip()
        content = request.POST.get('content').strip()
        if title in util.list_entries():
            return '<h1>already exist<h1/>'
        elif title == "" or content == "":
            return '<h1>empty Page.<h1/>'
        util.save_entry(title,content)
        return redirect('entry',title=title)
    
    return render(request,"encyclopedia/create.html" )
"""           
def edit(request,title):
    content = util.get_entry(title.strip())
    if content == "":
        return '<h1>empty content<h1/>'
    if request.method == 'GET':
        content = request.GET.get("content").strip()
        if content == "":
            return render(request, "encyclopedia/edit.html",{"error": "empty content.", "title": title, "content": content})
        
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})
"""

def edit(request, title):
    if request.method == 'POST':
        editContent = request.POST.get('content')
        if editContent.strip():
            util.save_entry(title,editContent)
            return redirect('entry',title=title)
        else:
            return render(request, 'edit.html', {
                'title': title,
                'error': 'empty content.',
                'content':editContent
            })
    else:
        previousContent = util.get_entry(title)
        return render(request, 'edit.html', {
            'title': title,
            'content': previousContent
        })
    
def search(request):
    pageQuery = request.POST.get('q')
    if pageQuery in util.list_entries():
        return redirect('entry',title=pageQuery)
    return render(request, "encyclopedia/search.html", {"entries": util.search(pageQuery), "q": pageQuery})


def randomPage(request):
    pages = util.list_entries()
    randmPage = random.choice(pages)
    return redirect('entry', title=randmPage)   