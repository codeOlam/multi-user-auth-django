from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from django.shortcuts import redirect
import datetime
from django.utils import timezone
import string
import random



def randomStrDig(strlen=4):
	"""
		Convenience methods to autogenerate string
	"""
	alpha_num 	= string.ascii_letters + string.digits

	return ''.join(random.choice(alpha_num) for i in range(strlen)).lower()

gen_str = randomStrDig()


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves user
        """
        if not email:
        	raise ValueError('Must provide a valid email address')

        now = timezone.now()
        user    = self.model(
                        email=email,
                        date_joined=now,
                        last_login=now,
                        **extra_fields
                            ) 

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email, username, password, **extra_fields):
        """
        Creates and saves superuser
        """
        user = self.model(
                          email = email,
                          username=username,
                          **extra_fields                         
                          )
        user.set_password(password)
        user.is_admin =True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser):
    u_id 		    = models.AutoField(primary_key=True, blank=True)      
    email 			= models.EmailField(max_length=127, unique=True, null=False, blank=False)
    username 		= models.CharField(max_length=15, help_text='A public user name', unique=True, blank=False, null=False)
    first_name      = models.CharField(max_length=50, blank=False, null=False)
    last_name       = models.CharField(max_length=50, blank=False, null=False)
    slug			= models.SlugField(unique=True, null=True, blank=True)
    date_joined     = datetime.datetime.now()
    is_admin 		= models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_usermodel1	= models.BooleanField(default=False)
    is_usermodel2	= models.BooleanField(default=False)
    is_active 		= models.BooleanField(default=True)
    

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = "accounts"
        db_table = "users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #User has a specific permission
        return True

    def has_module_perms(self, app_label):
        #User have permission to view app label
        return True

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'slug': self.slug})


@receiver(pre_save, sender=CustomUserModel)
def gen_slug(sender, instance, **kwargs):
    t = 'um1'
    instance.slug = slugify(instance.username+'_'+t)



class UserModel1(models.Model):
    user 			= models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True, blank=True)
    exec_postion	= models.CharField(max_length=50, blank=False, null=False)
    level 			= models.PositiveIntegerField()

    def __str__(self):
        return self.exec_postion 



class UserModel2(models.Model):
	user 			= models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True, blank=True)
	qualification	= models.CharField(max_length=50, blank=False, null=False)
	appointment		= models.CharField(max_length=50, blank=False, null=False)