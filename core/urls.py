from django.conf.urls import include, url
from .views import*

urlpatterns = (
                      url(r'^$', Home.as_view(), name='home'),
                      )