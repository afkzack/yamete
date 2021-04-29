from django.shortcuts import get_object_or_404, render, redirect
from .models import Videos, Episodes, Choice

def index(request):
	#latest_videos_list = Videos.objects.order_by('-pub_date')[:5]
	videos_list = Videos.objects.all()
	#videos = Videos.objects.all()
	context = {'videos_list': videos_list}
	#context = {'videos': videos}
	return render(request, 'proj/index.html', context)

def detail(request, videos_id):
	videos = get_object_or_404(Videos, pk=videos_id)
	episodes = Episodes.objects.all()
	return render(request, 'proj/detail.html', {'videos': videos, 'episodes':episodes})

def maintenance(request):
	return render(request, 'proj/maintenance.html')