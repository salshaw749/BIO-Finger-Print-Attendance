from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm 
from .models import Attendence
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



# this will show the main home page where user sign up , log in 
def home(request):
	return render(request,'fingerPrint/homeTemp.html')


# creat new user to the system
def signup(request):
	form= UserCreationForm()
	if request.method=='POST':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else: 
			form= UserCreationForm()

	return render(request, 'registration/signUp.html',{
		'form':form
		})


# def login_view(request):
	
# 	 return render(request, "fingerPrint/login.html")

# 	if request.method=="POST":
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			if user.is_active:
# 				login(request, user)
# 				return redirect('date')
	  
# 			# Redirect to a success page.
# 		else:
# 			# Return a 'disabled account' error message
	
# 				return (request,'invalid login') 
				

	



def date(request):
	
	return render(request, "fingerPrint/date.html")



def Attendence_recoreds(request): 
	records = Attendence.objects.all().order_by('date')
	return render(request,"fingerPrint/records.html",{'recoreds':records})



def Attendence_details (request, username):
	AttRecord=Attendence.objects.get(username=username)
	return render(request,"fingerPrint/Attrecord.html", {"attendence recored ":AttRecord})