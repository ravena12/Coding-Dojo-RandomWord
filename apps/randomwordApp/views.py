from django.shortcuts import render, redirect
import random 
import string

def index(request):
	return render(request, 'randomwordTemp/index.html')

def process(request):
	if 'counter' in request.session:
		request.session['counter'] +=1
	else:
		request.session['counter'] = 1
	request.session['randomstring'] = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for pos in range(0, 14))
	return redirect('/showResults')

	

def showResults(request):
	return render(request, 'randomwordTemp/index.html')
