from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserType(models.Model):
	usertype = models.CharField(max_length = 30, unique = True)
	user_count = models.IntegerField(default = 0)

	class Meta:
		verbose_name = _('UserType')
		verbose_name_plural = _('UserTypes')

	def __str__(self):
		return self.usertype

class UserManager(BaseUserManager):
	def create_user(self, email, password = None):
		if not email:
			raise ValueError("Email is not given")
		user = self.model(
				email = self.normalize_email(email),
			)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
				email = self.normalize_email(email),
				password = password,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using = self._db)
		return user

class User(AbstractBaseUser):
	username = None
	email = models.EmailField(verbose_name = "Email", max_length = 100, unique = True )
	name = models.CharField(verbose_name = "Name", max_length = 50)
	mobile = models.BigIntegerField(max_length=14, unique= True, blank = True, null = True, editable =True)
	is_admin = models.BooleanField(default = False)
	is_staff = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	user_type = models.ForeignKey(UserType, on_delete = models.DO_NOTHING, blank = True, null = True)

	class Meta:
		verbose_name = _('User')
		verbose_name_plural = _('Users')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

