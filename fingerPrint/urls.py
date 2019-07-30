from django.conf.urls import url, include
from . import views 
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

urlpatterns = [

	url(r'^$' , views.login_view),
	url(r'^$' , views.date),
	url(r'^$' , views.Attendence_recoreds),

	
]

