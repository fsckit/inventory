from django.conf.urls.defaults import *

# Routes for the different operations on a single customer; links a URI to a
# controller

urlpatterns = patterns('app.customer.views',
  url(r'^index/$', 'index', name='customer_index'),
  url(r'^create/$', 'create', name='customer_create'),
  url(r'^(\d+)/$', 'read', name='customer_read'),
  url(r'^(\d+)/update/$', 'update', name='customer_update'),
  url(r'^(\d+)/delete/$', 'delete', name='customer_delete'),
)
