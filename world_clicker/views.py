from django.shortcuts import render, HttpResponse, redirect
#from . import models

def start(request):
	return redirect('index')