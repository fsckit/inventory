from django.conf.urls.defaults import *

# Single view to add search controller
urlpatterns = patterns('app.search.views',
    url(r'^$', 'search', name='search_search'))
