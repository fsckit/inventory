from django.conf.urls.defaults import *

urlpatterns = patterns('app.staff.views',
  url(r'^create/$', 'create', name='staff_create'),
  url(r'^(\d+)/$', 'read', name='staff_read'),
  url(r'^update/$', 'update', name='staff_update'),
)

urlpatterns += patterns('django.contrib.auth.views',
  url(r'login/$', 'login', name='login'),
  url(r'logout/$', 'logout', name='logout'),
  url(r'password/reset/$', 'password_reset', name='pw_reset'),
  url(r'password/reset/done/$', 'password_reset_done', name='pw_reset_done'),
  url(r'password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', name='pw_reset_confirm'),
  url(r'password/reset/complete/$', 'password_reset_complete', name='pw_reset_complete'),
  url(r'password/change/$', 'password_change', name='pw_change'),
  url(r'password/change/complete/$', 'password_change_done', name='pw_change_done'),
)
