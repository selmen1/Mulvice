	
from django.shortcuts import render



def dashboard(request):

	templqte_name = 'dashboard.html'
	return render(request , templqte_name)