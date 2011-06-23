from django.conf.urls.defaults import *
from games.views import index

urlpatterns = patterns('',
   	url(r'^$', index, name='index'),
)