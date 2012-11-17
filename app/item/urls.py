from django.conf.urls.defaults import *

# Routes for the different operations on a single item; links a URI to a
# controller

urlpatterns = patterns('app.item.views',
  url(r'^index/$', 'index', name='item_index'),
  url(r'^create/$', 'create', name='item_create'),
  url(r'^(\d+)/$', 'read', name='item_read'),
  url(r'^(\d+)/update/$', 'update', name='item_update'),
  url(r'^delete/$', 'delete', name='item_delete'),
)
