from django.shortcuts 				import render,  get_object_or_404 ,redirect 
from django.contrib 				import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator 			import Paginator
from django.http                    import HttpResponse
from django.db.models               import Q
from .models 						import *
from .forms 						import *

# Create your views here.



@login_required
def profile(reqeust ):
	template_name = 'pages/profile.html'
	profile  = get_object_or_404(Profile  , pk = reqeust.user.pk)
		
	if reqeust.method == 'POST':
		form = ProfileForm(reqeust.POST or None , reqeust.FILES or None , instance=profile)
		
		try:
			if form.is_valid():
				form.save()
				
				return redirect('profile')
		except Exception as e:
				messages.warning(reqeust , 'the post was not save due to Error {}'.format(e))
	else:
		form = ProfileForm(instance=profile)
	context = { 'form' : form , 'profile':profile}
	return render(reqeust , template_name , context)




def service(reqeust ):
	template_name = 'pages/service.html'
	categories_list = CategorieService.objects.select_related('service', 'categorie', )
	query = reqeust.GET.get('q')
	query1 = reqeust.GET.get('q1')

	if query :
		categories_list = categories_list.filter(service__service_name =query)
	elif query1:
		categories_list = categories_list.filter(	categorie__libelle =query1)
	elif query and query1:
		categories_list = categories_list.filter(	Q(service__service_name =query)|
													Q(categorie__libelle=query1))


	paginator = Paginator(categories_list, 3) # Show 3 contacts per page
	page = reqeust.GET.get('page')

	categories = paginator.get_page(page)
	context = { 
				'categories':categories,
				 }
	return render(reqeust , template_name , context)



def service_detail(reqeust , pk):
	service = get_object_or_404(Service , pk = pk)

	args = {"service": service}

	return render(reqeust , 'pages/service_detail.html' , args)



@login_required
def create_service(reqeust):
	template_name = 'pages/create_service.html'

	profile = Profile.objects.get(  pk = reqeust.user.pk)

	form = ServiceForm(reqeust.POST or None )
	form1 = CategorieServiceForm(reqeust.POST or None)
	if form.is_valid() and form1.is_valid():
		instance = form.save(commit =False)
		instance.profile = profile
		instance.save()
		instance1 = form1.save(commit =False)
		instance1.service = instance
		instance1.save()

		return redirect('my_services')

		
	context = { 'form' : form ,'form1' : form1 ,  }
	return render(reqeust , template_name , context)




@login_required
def my_services(reqeust ):
	template_name = 'pages/my-service.html'
	profile = Profile.objects.get(  pk = reqeust.user.pk)

	service_list  = Service.objects.filter(profile = profile.pk)
	
	paginator = Paginator(service_list, 3) # Show 3 contacts per page
	page = reqeust.GET.get('page')

	services = paginator.get_page(page)
	
	context = {  'services':services}
	return render(reqeust , template_name , context)





@login_required
def my_services_detail(reqeust , pk ):
	template_name = 'pages/service_detail.html'

	profile = Profile.objects.get(  pk = reqeust.user.pk)
	service  = get_object_or_404(Service  , pk = pk)
	servcat = get_object_or_404(CategorieService, service = service)

	if reqeust.method == 'POST':
		form = ServiceForm(reqeust.POST or None , reqeust.FILES or None  , instance=service)
		form1 = CategorieServiceForm(reqeust.POST or None, reqeust.FILES or None, instance=servcat)
		
		try:
			if form.is_valid() and form1.is_valid():
				form.save()
				form1.save()
				
				return redirect('my_services')
		except Exception as e:
				messages.warning(reqeust , 'the post was not save due to Error {}'.format(e))
	else:
		form = ServiceForm(instance=service)
		form1 = CategorieServiceForm(instance=servcat)
		
	context = { 'form' : form ,'form1' : form1 , 'profile':profile}
	return render(reqeust , template_name , context)