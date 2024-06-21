from django.urls import path
#from .views import home, fetch_indian_railway_news, fetch_global_railway_news
from neews import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_indian_railway_news/', views.fetch_indian_railway_news, name='fetch_indian_railway_news'),
    path('fetch_global_railway_news/', views.fetch_global_railway_news, name='fetch_global_railway_news'),
]
