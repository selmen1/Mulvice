from rest_framework.serializers import ModelSerializer 
from rest_framework import serializers


from services.models import *

class ProfileSerializer(ModelSerializer):

	class Meta:
		model = Profile
		fields = [
			'id',
			'name',
			'lastname',
			'birth_date',
			'sexe',
			'diplome',


		]


class test(serializers.Serializer):

	service_name = serializers.CharField(max_length=200)
	langtitude = serializers.FloatField()
	latitude = serializers.FloatField()

class ServiceSerializer(ModelSerializer):

	class Meta:
		model = Service
		fields = [
			'langtitude',
			'latitude',
			'service_name',
			'discription',
			'wilaya',
			'comune',
			'email',
			'tel',
			'facebook',
			'instagram',


		]


class CategorieSerializer(ModelSerializer):

	class Meta:
		model = Categorie
		fields = [
			'libelle',
			'discription',
			]