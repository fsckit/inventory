from django.conf.urls.defaults import *

urlpatterns = patterns('app.transaction.views',
  url(r'^create$', 'create', name='transaction_create'),
  url(r'^(\d+)$', 'read', name='ctransaction_read'),
  url(r'^(\d+)/update$', 'update', name='transaction_update'),
  url(r'^(\d+)/delete$', 'delete', name='transaction_delete'),
)
