from django import forms
from .models import *




class ProfileForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
	birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control docs-date','placeholder':'MM/JJ/AAAA'}), required = False )
	sexe = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
	diplome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }), required = False)
	# formation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
	tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)

	class Meta:
		model = Profile
		fields = (
				 'name', 
				 'lastname',
				 'birth_date',
				 'sexe',
				 'diplome',
				 'formation',
				 'tel',
				 'picture',

				 )



class ServiceForm(forms.ModelForm):
	
	latitude = forms.CharField(widget=forms.TextInput(attrs={'id':'lat'}))
	langtitude = forms.CharField(widget=forms.TextInput(attrs={'id':'lang'}))
	class Meta:
		model = Service
		fields = ( 
				 'service_name', 
				 'discription',
				 'wilaya',
				 'comune',
				 'latitude',
				 'langtitude',
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
