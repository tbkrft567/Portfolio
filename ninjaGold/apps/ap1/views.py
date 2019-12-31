from django.shortcuts import render, redirect
import random

def index(request):
    if 'totalGold' not in request.session: # SET GOLD AND ATTEMPTS = 0 AT SCREEN_LOAD
        request.session['totalGold'] = 0
    if 'attempts' not in request.session: 
        request.session['attempts'] = 0

    # request.session.flush()
    return render(request, 'ap1/index.html')

def process(request, building):
    if building == 'process': # VALUE PASS BY BUTTON
        request.session['userInput'] = request.POST['building']
    else:                       # VALUE PASS BY URL
        request.session['userInput'] = building
    
    if request.session['userInput'] == 'farm':
        request.session['gold'] = random.randint(10,20)
    if request.session['userInput'] == 'cave':
        request.session['gold'] = random.randint(5,10)
    if request.session['userInput'] == 'house':
        request.session['gold'] = random.randint(2,5)
    if request.session['userInput'] == 'casino':
        request.session['gold'] = random.randint(-50,50)

    request.session['totalGold'] += request.session['gold']
    
    request.session['attempts'] += 1



    if int(request.session['attempts']) == int(request.session['tries']): # CHECK WETHER USER HAS EXHAUSTED ALL ATTEMPTS TO END GAME
        if int(request.session['totalGold']) >= int(request.session['goldGoal']):
            request.session['completionMessage'] = "You did it!!"
        else:
            request.session['completionMessage'] = "Sorry, you didn't make it!!"
    else:
        pass    

    if 'activities' in request.session: 
        request.session['activities'] = 'Earned '+str(request.session['gold'])+' golds from the '+request.session['userInput']+'!\n' +request.session['activities']
    else:
        request.session['activities'] = 'Earned '+str(request.session['gold'])+' golds from the '+request.session['userInput']+'!\n'

    return redirect('/')

def settings(request): # STORE GAME CRITERIA
    request.session['goldGoal'] = request.POST['goldGoal']
    request.session['tries'] = request.POST['countGoal']
    
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')