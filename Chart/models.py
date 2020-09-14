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
		