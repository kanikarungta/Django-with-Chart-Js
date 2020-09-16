from django.shortcuts import render
from django.http import HttpResponse
from .models import UserType, User
from django.contrib import messages

# Create your views here.
def index(request):
	roles = UserType.objects.all()
	ides = UserType.objects.all().values_list('id', flat = True)
	cons = ides.count()
	for i in range(cons):
		usre = User.objects.filter(user_type = ides[i])
		countr = usre.count()
		role = UserType.objects.get(id = ides[i])
		role.user_count = 0
		role.user_count+=countr
		role.save()

	if request.method == 'POST':
		email = request.POST.get('email')
		name = request.POST.get('name')
		mobile = request.POST.get('mobile')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		user_type = request.POST.get('user_type')

		if password1 == password2:
			if User.objects.filter(email = email).exists():
				messages.info(request, "Email taken")
				return render(request, "base.html", {'roles': roles})
			else:
				user = User(email=email, name = name, mobile = mobile, user_type = UserType.objects.get(id = user_type))
				user.set_password(password1)
				user.save()
				ids = UserType.objects.all().values_list('id', flat = True)
				con = ids.count()
				for i in range(con):
					usr = User.objects.filter(user_type = ids[i])
					counter = usr.count()
					role = UserType.objects.get(id = ids[i])
					role.user_count = 0
					role.user_count+=counter
					role.save()
				return render(request, 'base.html', {'roles': roles})
		else:
			messages.info(request, "Password do not Match")
			return render(request, 'base.html', {'roles': roles})

	return render(request, 'base.html', {'roles': roles})
	
