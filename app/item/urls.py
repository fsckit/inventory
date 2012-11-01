from django.conf.urls.defaults import *

urlpatterns = patterns('app.item.views',
  url(r'^index/$', 'index', name='item_index'),
  url(r'^create/$', 'create', name='item_create'),
  url(r'^(\d+)/$', 'read', name='item_read'),
  url(r'^update/$', 'update', name='item_update'),
  url(r'^delete/$', 'delete', name='item_delete'),
)
