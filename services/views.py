from django.shortcuts 				import render,  get_object_or_404 ,redirect 
from django.contrib 				import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator 			import Paginator
from django.http                    import HttpResponse ,JsonResponse
from django.db.models               import Q
from .models 						import *
from .forms 						import *
from . 								import views
from django.core.mail 				import send_mail, BadHeaderError


# Create your views here.



@login_required
def profile(reqeust ):
	template_name = 'pages/profile.html'
	profile  = get_object_or_404(Profile  , pk = reqeust.user.pk)
		
	if reqeust.method == 'POST':
		form = ProfileForm(reqeust.POST or None , reqeust.FILES or None ,instance=profile)
		
		try:
			if form.is_valid():
				form.save()
				print('profile saved')
				
				return redirect('profile')
		except Exception as e:
				messages.warning(reqeust , 'the post was not save due to Error {}'.format(e))
	else:
		form = ProfileForm(instance=profile)
	context = { 'form' : form , 'profile':profile}
	return render(reqeust , template_name , context)




def service(reqeust ):
	template_name = 'pages/service.html'
	categories_list = Service.objects.all()
	categorie_options = Categorie.objects.all()
	query = reqeust.GET.get('q')
	query1 = reqeust.GET.get('q1')
	query2 = reqeust.GET.get('q2')

	if query :
		categories_list = categories_list.filter(service_name =query)
	elif query1:
		categories_list = categories_list.filter(	categorie__libelle =query1)
	elif query2:
		categories_list = categories_list.filter(	Q(wilaya =query2)|Q(comune =query2))
	elif query and query1  : 
		categories_list = categories_list.filter(	Q(service_name =query)|
													Q(libelle=query1))
	elif query and query2  : 
		categories_list = categories_list.filter(	Q(service_name =query)|
													Q(wilaya =query2)|Q(comune =query2))
	elif query1 and query2  : 
		categories_list = categories_list.filter(	Q(libelle=query1)|
													Q(wilaya =query2)|Q(comune =query2))
	elif query1 and query2 and query : 
		categories_list = categories_list.filter(	Q(service_name=query)|
													Q(libelle=query1)|
													Q(wilaya =query2)|Q(comune =query2))
	# json = []
	# for c in categories_list:
	# 	s = test(c.service)
	# 	json.append(s.data)


	paginator = Paginator(categories_list, 3) # Show 3 contacts per page
	page = reqeust.GET.get('page')

	categories = paginator.get_page(page)
	context = { 
				'categories':categories,
				'categories_list':categories_list,
				'categorie_options':categorie_options,

				 }
	return render(reqeust , template_name , context)



def service_detail(reqeust , pk):
	service = get_object_or_404(Service , pk = pk)
	profile_id = service.profile.id
	profile = Profile.objects.get(pk = profile_id)
	print(profile)
	profile_form = ProfileDetailForm(instance=profile)
	form = ServiceDetailForm(instance=service)
	args = {"service": service , 'form':form , 'profile_form':profile_form}

	return render(reqeust , 'pages/service_detail.html' , args)



@login_required
def service_del(reqeust , pk):
	service  = get_object_or_404(Service , pk = pk)
	service.delete()
	return redirect('my_services')


@login_required
def create_service(reqeust):
	template_name = 'pages/create_service.html'

	profile = Profile.objects.get(  pk = reqeust.user.pk)
	form = ServiceForm(reqeust.POST or None )
	if reqeust.method == 'POST':
		
		if form.is_valid() :
			instance = form.save(commit =False)
			instance.profile = profile
			instance.save()
			instance.categorie.set(reqeust.POST.get('categorie'))
			
			return redirect('my_services')
	

		
	context = { 'form' : form  }
	return render(reqeust , template_name , context)




@login_required
def my_services(reqeust ):
	template_name = 'pages/my-service.html'
	profile = Profile.objects.get(  pk = reqeust.user.pk)

	services  = Service.objects.filter(profile = profile.pk)
	
	
	context = {  'services':services}
	return render(reqeust , template_name , context)





@login_required
def my_services_detail(reqeust , pk ):
	template_name = 'pages/service_detail.html'

	profile = Profile.objects.get(  pk = reqeust.user.pk)
	service  = get_object_or_404(Service  , pk = pk)

	if reqeust.method == 'POST':
		form = ServiceForm(reqeust.POST or None , reqeust.FILES or None  , instance=service)
		print(reqeust.POST.get('categorie'))
		try:
			if form.is_valid() :
				form.save()
				
				return redirect('my_services')
		except Exception as e:
				messages.warning(reqeust , 'the post was not save due to Error {}'.format(e))
	else:
		form = ServiceForm(instance=service)
		
	context = { 'form' : form , 'service':service, 'profile':profile}
	return render(reqeust , template_name , context)





def get_data(reqeust , *d , **dd):
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
	
	
	models =    []
	geojson = {}
	for c in categories_list:
		models.append(c)
		
	geojson["type"] = "FeatureCollection"	
	geojson["features"] = []

	for x in models:

		geojson["features"].append({
								   "type":"Feature", 
								   "properties": 
								   		{
								   		"type": str(x.categorie.libelle),
								   		  }, 
								   	"geometry": 
								   		{ "type": "Point", 
								   		  "coordinates":[ x.service.langtitude, x.service.latitude] 
								   		  } 
								   })

	return JsonResponse(geojson)




def contact_us(reqeust):
	template_name = 'pages/contact_us.html'


	if reqeust.method == 'POST':
		form = ContactUsForm(reqeust.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['localhost'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('contact_us')

	else:
		form = ContactUsForm()


	args = {'form' : form , }

	return render(reqeust , template_name , args)


