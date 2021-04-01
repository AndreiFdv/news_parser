from django.urls import path

from News import views

app_name = 'News'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.DetailView.as_view(), name='detail')
]
