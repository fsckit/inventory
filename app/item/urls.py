from django.conf.urls.defaults import *

urlpatterns = patterns('app.item.views',
  url(r'^create/$', 'create', name='item_create'),
  url(r'^(\d+)/$', 'read', name='item_read'),
  url(r'^(\d+)/update/$', 'update', name='item_update'),
  url(r'^(\d+)/delete/$', 'delete', name='item_delete'),
)
