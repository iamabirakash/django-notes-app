from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import *

def LPU(request):
    notes = Note.objects.all()
    return render(request, 'index.html',{'notes':notes})

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("wowowowow")

def save_data(request):
    # print(request.POST)
    title = request.POST.get("title", "")
    description = request.POST.get("description", "")
    if not title or not description:
            messages.error(request, "Fill all details")
            return redirect("/")
    note = Note(title=title,description=description)
    note.save()
    messages.success(request,"Details Saved")
    return redirect("/")

def indexView(request):
    notes = Note.objects.all()
    return render(request,"index.html",{'notes':notes})

def deleteView(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    messages.success(request, "Note deleted")
    return redirect("/")

def editView(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == "POST":
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")

        if not title or not description:
            messages.error(request, "Fill all details")
            return redirect(f"/edit/{id}/")

        note.title = title
        note.description = description
        note.save()

        messages.success(request, "Note updated successfully")
        return redirect("/")

    return render(request, "edit.html", {"note": note})
