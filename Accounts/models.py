from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your tests here.

class UserManager(BaseUserManager ):
    def create_user(self , email , password = None , is_staff = False , is_admin=False , is_active = True):
        if not email:
            raise ValueError('user must have an email adresse')
        user_obj = self.model(
            email = self.normalize_email(email),
                    )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using = self._db)
        return user_obj

    def create_staffuser(self , email  , password=None):
        user = self.create_user(
            email ,
            
            password,
            is_staff=True,
            is_active = True
            )
        return user

    def create_superuser(self , email , password=None):
        user = self.create_user(
            email ,
            
            password,
            is_staff=True,
            is_admin =True,
            is_active = True
            )
        return user






class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=False)
    staff    = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.


    def get_full_name(self):
    # The user is identified by their email address
    	return self.email


    def get_short_name(self):
    # The user is identified by their email address
    	return self.email

    def __str__(self):
    	return self.email

    def has_perm(self, perm, obj=None):
    	"Does the user have a specific permission?"
    	# Simplest possible answer: Yes, always
    	return True


    def has_module_perms(self, app_label):
    	"Does the user have permissions to view the app `app_label`?"
    	# Simplest possible answer: Yes, always
    	return True

    @property
    def is_staff(self):
    	"Is the user a member of staff?"
    	return self.staff


    @property
    def is_admin(self):
    	"Is the user a admin member?"
    	return self.admin

    @property
    def is_active(self):
    	"Is the user active?"
    	return self.active



    objects = UserManager()



