from django.conf.urls.defaults import *

urlpatterns = patterns('app.staff.views',
		url(r'^create/$', 'create', name='staff_create'),
		url(r'^(\d+)/$', 'read', name='staff_read'),
		url(r'^(\d+)/update/$', 'update', name='staff_update'),
		url(r'^(\d+)/delete/$', 'delete', name='staff_delete')
)
