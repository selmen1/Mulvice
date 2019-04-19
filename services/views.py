from django.shortcuts import render

# Create your views here.



def all_services(request):

	templqte_name = 'services/all_services.html'
	return render(request , templqte_name)



def create_service(request):

	templqte_name = 'services/create_service.html'
	return render(request , templqte_name)



