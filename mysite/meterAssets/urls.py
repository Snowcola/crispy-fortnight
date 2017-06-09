from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.meter_data_list, name='meter_data_list'),
]