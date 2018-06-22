from django.urls import path

from . import views
from . import getresults
urlpatterns = [
#	path('', views.probe, name='probe'),
	path('', views.index, name='index'),
	path('', views.second, name='second')
#	path('', views.submit, name='submit'),

]