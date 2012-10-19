from django.conf.urls.defaults import *

urlpatterns = patterns('app.customer.views',
  url(r'^create$', 'create', name='customer_create'),
  url(r'^(\d+)$', 'read', name='customer_read'),
  url(r'^(\d+)/update$', 'update', name='customer_update'),
  url(r'^(\d+)/delete$', 'delete', name='customer_delete'),
)
