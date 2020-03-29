from django.urls import path
from django.conf.urls import url
from . import views




urlpatterns = [
    path('', views.index, name='index'),
	#path('#' , views.add, name = "click"),
	path("r",views.add, name="test"),
	path("update", views.update, name="update"),
	
	
	
]