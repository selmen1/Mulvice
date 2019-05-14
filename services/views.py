from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request,'services/home.html')

class DashboardView(TemplateView):
    """docstring for DashboardView"""
    template_name='services/dashboard.html'

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid() :
			form.save()
			return redirect('login')

	else:
		form=UserCreationForm()


	args={'form':form}
	return render(request,'services/reg_form.html',args)		