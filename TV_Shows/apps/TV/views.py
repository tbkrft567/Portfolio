from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'TV\index.html', context)

def create(request):
    return render(request, 'TV\create.html')

def show(request, id):
    context= {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'TV\show.html', context)

def createProcess(request):
    errors = Show.objects.basic_validator(request.POST)
    titleValidation = Show.objects.duplicateTitle(request.POST, id)
    print(titleValidation)
    if len(errors)>=1 or len(titleValidation)>=1:
        for key, value in titleValidation.items():
            messages.error(request, value)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['releaseDate'], description=request.POST['description'])
        createdId = Show.objects.last().id
        return redirect('shows/'+str(createdId))

def edit(request, id):
    context={
        'show': Show.objects.get(id=id),
        'pythonDate': Show.objects.get(id=id).release_date,
    }
    return render(request, 'TV\edit.html', context)

def delete(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/')

def editProcess(request, id):
    errors = Show.objects.basic_validator(request.POST)
    titleValidation = Show.objects.duplicateTitle(request.POST, id)
    print(titleValidation)
    if len(errors)>=1 or len(titleValidation)>=1:
        for key, value in titleValidation.items():
            messages.error(request, value)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')
    else:
        print(Show.objects.get(id=id).title)
        updateFields = Show.objects.get(id=id)
        updateFields.title = request.POST['title']
        updateFields.network = request.POST['network']
        updateFields.release_date = request.POST['releaseDate']
        updateFields.description = request.POST['description']
        updateFields.save(update_fields=['title', 'network', 'release_date', 'description'])
        # Show.objects.get(id=id).network = request.POST['network']
        # Show.objects.get(id=id).release_date = request.POST['release_date']
        # Show.objects.get(id=id).description = request.POST['description']
    return redirect('/shows/'+str(id))
