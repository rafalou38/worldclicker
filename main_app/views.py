from django.shortcuts import render, HttpResponse, redirect
from . import models
from math import log, floor
from django.http import JsonResponse




def human_format(number):
	units = ['', 'K', 'M', 'B', 'T', 'Q' , 'Sex', 'Sep', 'O', 'N', 'D']
	k = 1000.0
	magnitude = int(floor(log(number, k)))
	return '%.2f%s' % (number / k**magnitude, units[magnitude])


# Create your views here.
world = models.world.objects.get(id=1)
def add(request):

	world.cliks = world.cliks + 1
	world.save()
	return redirect("index")
def index(request):

	return render(request, 'index.html', {"cli":human_format(world.cliks), 'bcli':world.cliks} )

def update(request):
	world.cliks = world.cliks + 1
	world.save()
	#print(request.GET.get('username'))

	return JsonResponse({'clicks': world.cliks})


