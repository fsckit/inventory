from django.conf.urls.defaults import *

# Routes for the different operations on a single transaction; links a URI to a
# controller

urlpatterns = patterns('app.transaction.views',
  url(r'^index/$', 'index', name='transaction_index'),
  url(r'^create/$', 'create', name='transaction_create'),
  url(r'^(\d+)/$', 'read', name='transaction_read'),
  url(r'^(\d+)/update/$', 'update', name='transaction_update'),
  url(r'^(\d+)/delete/$', 'delete', name='transaction_delete'),
)
