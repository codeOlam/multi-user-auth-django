from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
import datetime
from django.utils import timezone



class UserManager(BaseUserManager):
    use_in_migrations = True

    
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves user
        """
        if not email:
        	raise ValueError('Must provide a valid email address')

        now = timezone.now()
        user    = self.model(
                        email=self.normalize_email(email),
                        date_joined=now,
                        last_login=now,
                        **extra_fields
                            ) 

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves superuser
        """
        user = self.model(
                          email = email,
                          **extra_fields                         
                          )
        user.set_password(password)
        user.is_admin =True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    u_id 		    = models.AutoField(primary_key=True, blank=True)      
    email 			= models.EmailField(max_length=127, unique=True, null=False, blank=False)
    username 		= models.CharField(max_length=15, help_text='A public user name', blank=True, null=True)
    first_name      = models.CharField(max_length=50, blank=False, null=False)
    last_name       = models.CharField(max_length=50, blank=False, null=False)
    date_joined     = datetime.datetime.now()
    is_admin 		= models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_usertype_a	= models.BooleanField(default=False)
    is_usertype_b	= models.BooleanField(default=False)
    is_active 		= models.BooleanField(default=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'   
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "accounts"
        db_table = "users"
        verbose_name = 'Users Account'
        verbose_name_plural = 'Users Account'



    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #User has a specific permission
        return True

    def has_module_perms(self, app_label):
        #User have permission to view app label
        return True

    def get_absolute_url(self):
        return reverse('accounts:uta_profile', kwargs={'pk': self.u_id})



class UserTypeA(models.Model):
    user 			= models.OneToOneField(Users, on_delete=models.CASCADE, related_name='user_type_a')
    exec_postion	= models.CharField(max_length=50, blank=False, null=False)
    level 			= models.PositiveIntegerField()

    def __str__(self):
        return self.exec_postion

    class Meta:
        verbose_name = 'Users Type A Account'
        verbose_name_plural = 'Users Type A Account' 



class UserTypeB(models.Model):
    user 			= models.OneToOneField(Users, on_delete=models.CASCADE, related_name='user_type_b')
    qualification	= models.CharField(max_length=50, blank=False, null=False)
    appointment		= models.CharField(max_length=50, blank=False, null=False)


    class Meta:
        verbose_name = 'Users Type B Accont'
        verbose_name_plural = 'Users Type B Account'