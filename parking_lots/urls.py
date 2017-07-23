from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home, name = 'Home'),
	# url(r'add_log/', views.Add_log, name = 'Add_log'),
	# url(r'update_status/', views.update_status, name = 'update_status'),
	# url(r'get/', views.get_duration, name = 'get_duration'),
]
