from django.shortcuts import render, HttpResponse, redirect 
from . import models
from math import log, floor
from django.http import JsonResponse
from django.template.loader import render_to_string
from django_ajax.decorators import ajax




def human_format(number):
	units = ['', 'K', 'M', 'B', 'T', 'Q' , 'Sex', 'Sep', 'O', 'N', 'D']
	k = 1000.0
	magnitude = int(floor(log(number, k)))
	return '%.2f%s' % (number / k**magnitude, units[magnitude])


# Create your views here.
world = models.world.objects.get(id=1)

def index(request):
	return render(request, 'index.html', {"cli":human_format(world.cliks), 'bcli':world.cliks} )





def update(request):
	world.cliks = world.cliks + 1
	world.save()
	#print(request.GET.get('username'))

	return JsonResponse({'clicks': world.cliks})

# yourapp.views.py

# from django.views.generic import FormView

# from .forms import JoinForm


# class JoinFormView(FormView):
#     form_class = JoinForm
#     template_name  = 'ajax.html'
#     success_url = '/form-success/'
# 	def form_invalid(self, form):
#         response = super(JoinFormView, self).form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response

#     def form_valid(self, form):
#         response = super(JoinFormView, self).form_valid(form)
#         if self.request.is_ajax():
#             print(form.cleaned_data)
#             data = {
#                 'message': "Successfully submitted form data."
#             }
#             return JsonResponse(data)
#         else:
#             return response

