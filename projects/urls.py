from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [

	path('', views.index, name='index'),
	path('<int:videos_id>/', views.detail, name='detail'),
	path('maintenance/', views.maintenance, name='maintenance'),

]

