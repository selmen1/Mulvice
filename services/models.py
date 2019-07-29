from django.db import models
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from Accounts.models import User
# Create your models here.
<<<<<<< HEAD

### ------profile model-----------------------------------
class Profile(models.Model):
	user = models.OneToOneField(User , 	 on_delete=models.CASCADE)
	name = models.CharField(max_length=250, blank=True)
	lastname = models.CharField(max_length=250, null=True,blank=True)
	birth_date = models.DateField(null=True,blank=True)
	picture = models.FileField(blank=True )
	sexe = models.CharField(max_length=50,null=True, blank=True )
	diplome = models.CharField(max_length=250, null=True,blank=True)
	creation_date	= models.DateField( auto_now_add= True,blank=True)
	def __str__(self):
		return 'Profile : {}'.format(self.user)

	def get_full_name(self):
		return '{} {}'.format(self.lastname , self.name)



@receiver(post_save , sender=User)
def create_user_profile(sender , instance , created , **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save , sender=User)
def save_user_profile(sender , instance , **kwargs):
	instance.profile.save()




### ------profile model-----------------------------------


# --------- service --------------


class Service(models.Model):

	profile = models.ForeignKey(Profile ,on_delete=models.CASCADE)
	slug = models.SlugField(unique = True)
	langtitude = models.IntegerField(null=True, blank=True)
	latitude = models.IntegerField(null=True, blank=True)
	service_name = models.CharField(max_length=50, blank=True)
	discription = models.CharField(max_length=250, blank=True)
	wilaya 			= models.CharField(max_length=50, null=True,blank=True)
	comune			= models.CharField(max_length=50,null=True, blank=True)
	cover_pic 		= models.FileField(null=True,blank=True )
	email 			= models.EmailField(null=True,blank=True )
	tel 			= models.CharField(max_length=12, null=True,blank=True )
	facebook 		= models.CharField(max_length=50,null=True, blank=True)
	instagram 		= models.CharField(max_length=50,null=True, blank=True)
	creation_date	= models.DateField( auto_now_add= True) 
	def __str__(self):
		return self.slug

def create_slug(instance , new_slug = None):
	slug  = slugify(instance.service_name)
	if new_slug is not None:
		slug = new_slug
	qs  = Service.objects.filter(slug = slug).order_by('-id')
	exists = qs.exists()
	if exists: 
		new_slug = "%s-%s" %(slug , qs.first().id)
		return create_slug(instance , new_slug=new_slug)

	return slug


def pre_save_post_receiver(sender , instance , **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver , sender=Service)


# --------- categorie --------------
class Categorie(models.Model):
	libelle = models.CharField(max_length=50, blank=True)
	discription = models.CharField(max_length=250, blank=True)
	icon =  models.FileField(null=True,blank=True )
	def __str__(self):
		return self.libelle

# --------- categorie --------------

class CategorieService(models.Model):
	categorie = models.ForeignKey(Categorie ,on_delete=models.CASCADE)
	service = models.ForeignKey(Service ,on_delete=models.CASCADE)
	class Meta:
		unique_together = (("categorie", "service"),)

=======
from django.contrib.auth.models import User

'''class Profil(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user.username) '''
>>>>>>> pre-prod
