from django.conf.urls.defaults import *

urlpatterns = patterns('app.search.views',
    url(r'^$', 'search', name='search_search'))
