from django.views.generic.list import ListView
from django.utils import timezone

from .models import NewsItem



class NewsItemListView(ListView):
	models = NewsItem
	template_name = 'news_item_list.html'


	def get_queryset(self):
		return NewsItem.objects.all()