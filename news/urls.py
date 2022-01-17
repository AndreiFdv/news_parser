from django.urls import path

from news import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('subscribe/', views.SubscriberView.as_view(), name='subscribe')

]
