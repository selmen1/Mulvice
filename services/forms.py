from django import forms
from .models import *




class ProfileForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
	birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control docs-date','placeholder':'MM/JJ/AAAA'}), required = False )
	sexe = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
	diplome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }), required = False)
	formation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)
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


class ProfileDetailForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}), required = False)
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}), required = False)
	birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control docs-date','placeholder':'MM/JJ/AAAA', 'disabled':'disabled'}), required = False )
	sexe = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}), required = False)
	diplome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'disabled':'disabled'}), required = False)
	formation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}), required = False)
	tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}), required = False)

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

				 )



class ServiceForm(forms.ModelForm):
	

	service_name = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control'}))
	discription = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control'}))
	wilaya 		= forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control'}))
	comune = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control'}))
	categorie = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={ 'class':'form-control' ,
																						'id':'cat-multiselect' , 
																						'multiple':'multiple' , 
																						'style':'width: 500px;'}),
                                          queryset= Categorie.objects.all())
	latitude = forms.CharField(widget=forms.TextInput(attrs={'id':'lat' , 'class':'form-control'}))
	langtitude = forms.CharField(widget=forms.TextInput(attrs={'id':'lang', 'class':'form-control'}))
	
	class Meta:
		model = Service
		fields = ( 
				 'service_name', 
				 'discription',
				 'wilaya',
				 'comune',
				 'latitude',
				 'langtitude',
				 'categorie',
				 'cover_pic',
				 )


class ServiceDetailForm(forms.ModelForm):
	

	service_name = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control' , 'disabled':'disabled'}))
	discription = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control', 'disabled':'disabled'}))
	wilaya 		= forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control', 'disabled':'disabled'}))
	comune = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control', 'disabled':'disabled'}))
	categorie = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={ 'class':'form-control' ,
																						'id':'cat-multiselect' , 
																						'multiple':'multiple' , 
																						'style':'width: 500px;', 
																						'disabled':'disabled'}),
                                          queryset= Categorie.objects.all())
	latitude = forms.CharField(widget=forms.TextInput(attrs={'id':'lat' , 'class':'form-control', 'disabled':'disabled'}))
	langtitude = forms.CharField(widget=forms.TextInput(attrs={'id':'lang', 'class':'form-control', 'disabled':'disabled'}))
	
	class Meta:
		model = Service
		fields = ( 
				 'service_name', 
				 'discription',
				 'wilaya',
				 'comune',
				 'latitude',
				 'langtitude',
				 'categorie',
				 'cover_pic',
				 )



class ContactUsForm(forms.Form):
	from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control ', }),required=True, label='Email')
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }),required=True, label='Sujet')
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'style':'height : 100px; color: #000 important!' }) ,  required=True , label='Message')