from django.urls import path


from .views import NewsItemListView

urlpatterns = [
	path('', NewsItemListView.as_view(), name='news-item-list'),
]
