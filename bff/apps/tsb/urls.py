#urls for tsb
from django.conf.urls import patterns, include, url
from tsb.views import SampleList

urlpatterns = patterns("",
                       url(r'^$', SampleList.as_view(), name ='sample-list'),
                       )