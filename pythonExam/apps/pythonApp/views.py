from django.shortcuts import render, redirect
from .models import User, UserManager, Quote
from django.contrib import messages
import bcrypt

def index(request):
    context={
        'users': User.objects.all()

    }
    # context['users'].delete()
    # request.session.flush()
    # Q = Quote.objects.all()
    # Q.delete()
    return render(request, 'pythonApp\index.html', context)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pwCrypt = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(firstName=request.POST['firstName'], lastName=request.POST['lastName'], email=request.POST['email'], password=pwCrypt)
    return redirect('/')

def loginAttempt(request):
    emailFound = User.objects.filter(email=request.POST['email'])
    if emailFound:
        userLogged = emailFound[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogged.password.encode()):
            request.session['userid'] = userLogged.id
            return redirect('/dashboard')
    if 'userid' not in request.session:
        messages.error(request, 'Password or Email not found in the database')
    return redirect('/')

def dashboard(request):
    if 'userid' not in request.session:
        messages.error(request, 'Password and Email must be entered to log in')
        return redirect('/')
    context={
        'user': User.objects.get(id=request.session['userid']),
        'nonFav_quotes': Quote.objects.exclude(favorited_by=User.objects.get(id=request.session['userid'])),
        'myFav_quotes': Quote.objects.filter(favorited_by=User.objects.get(id=request.session['userid'])),
    }

    return render(request, 'pythonApp/Dashboard.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def createQuote(request):
    errors = Quote.objects.quoteValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')
    print('created')
    Quote.objects.create(quote_text=request.POST['quote_text'], quoted_by=request.POST['quoted_by'], creator=User.objects.get(id=request.session['userid']))
    return redirect('/dashboard')

def userQuotes(request, userId):
    if 'userid' not in request.session:
        messages.error(request, 'Password and Email must be entered to log in')
        return redirect('/')
    context={
        'user': User.objects.get(id=userId),
        'quotes': Quote.objects.filter(creator=User.objects.get(id=userId))
    }
    return render(request, 'pythonApp/userQuotes.html', context)

def editQuotes(request, quoteId):
    quoteToEdit = Quote.objects.get(id=quoteId)
    if quoteToEdit.creator.id != request.session['userid']:
        print('Not Today, Zach!')
        return redirect('/dashboard')
    context={
        'quote': Quote.objects.get(id=quoteId)
    }
    return render(request, 'pythonApp/editQuote.html', context)

def updateQuotes(request, quoteId):
    errors = Quote.objects.quoteValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+quoteId)

    updateFields = Quote.objects.get(id=quoteId)
    updateFields.quote_text = request.POST['quote_text']
    updateFields.quoted_by = request.POST['quoted_by']
    updateFields.save(update_fields=['quoted_by', 'quote_text'])
    return redirect('/dashboard')

def delete(request, quoteId):
    quoteToDelete = Quote.objects.get(id=quoteId)
    print(quoteToDelete.creator.id)
    print(request.session['userid'])
    if quoteToDelete.creator.id != request.session['userid']:
        print('Not Today, Zach!')
        return redirect('/dashboard')
    else:
        quoteToDelete.delete()
    return redirect('/dashboard')

def addFav(request, quoteId):
    quoteFilter = Quote.objects.filter(id=quoteId)
    if quoteFilter:
        Quote.objects.get(id=quoteId).favorited_by.add(User.objects.get(id=request.session['userid']))
    else:
        print('This quote ID does not exist.')
    return redirect('/dashboard')

def removeFav(request, quoteId):
    quoteFilter = Quote.objects.filter(id=quoteId)
    if quoteFilter:
        Quote.objects.get(id=quoteId).favorited_by.remove(User.objects.get(id=request.session['userid']))
    else:
        print('This quote ID does not exist.')
    return redirect('/dashboard')