from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('contact', views.ContactUsView.as_view(), name='contact'),
]
