from django.shortcuts import render
from django.http import HttpResponse
from .models import UserType, User

# Create your views here.
def index(request):
	ids = UserType.objects.all().values_list('id', flat = True)
	con = ids.count()
	for i in range(con):
		usr = User.objects.filter(user_type = ids[i])
		counter = usr.count()
		role = UserType.objects.get(id = ids[i])
		role.user_count = 0
		role.user_count+=counter
		role.save()
		print("success")
	
