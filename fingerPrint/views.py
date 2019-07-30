from django.shortcuts import render, HttpResponse,redirect,get_object_or_404, get_list_or_404
from django.contrib.auth.forms import UserCreationForm 
from .models import Checkinout1, Userinfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import datetime



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

			return render(request, 'registration/signUp.html',{'form':form})

def is_valed_queryParam(param):
	return param !='' and param is not None

def date(request):

	attendance = Checkinout1.objects.filter( pk=request.user.first_name)
	S=request.GET.get('startDate')
	E=request.GET.get('endDate')

	# sdate=datetime.datetime.strptime(S,"%Y-%m-%d").date()
	# edate=datetime.datetime.strptime(E,"%Y-%m-%d").date()

	if  (S):
		attendance = attendance.filter(date__gte=datetime.datetime.strptime(S,"%m/%d/%Y").strftime("%Y%m%d"))

	if  (E):
		attendance = attendance.filter(date__lte=datetime.datetime.strptime(E,"%m/%d/%Y").strftime("%Y%m%d"))

	# attendance= attendance.filter(date__gte='startDate' )
	# attendance= attendance.filter(date__lte='endDate' )
	return render(request , "fingerPrint/date.html" ,{'attendance' : attendance})



