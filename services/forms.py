from django import forms
from .models import *




class ProfileForm(forms.ModelForm):
	

	class Meta:
		model = Profile
		fields = (
				 'name', 
				 'lastname',
				 'birth_date',
				 'sexe',
				 'diplome',
				 'picture',

				 )



class ServiceForm(forms.ModelForm):
	

	class Meta:
		model = Service
		fields = ( 
				 'service_name', 
				 'discription',
				 'wilaya',
				 'comune',
				 'email',
				 'tel',
				 'facebook',
				 'instagram',
				 'cover_pic',
				 )


class CategorieServiceForm(forms.ModelForm):
	

	class Meta:
		model = CategorieService
		fields = ( 
				 'categorie', 
				 
				 )
