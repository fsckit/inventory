from django.conf.urls.defaults import *

urlpatterns = patterns('app.staff.views',
		url(r'^login/$', 'login', name='staff_login'),
		url(r'^logout/$', 'logout', name='staff_logout'),
		url(r'^changepwd/$', 'changepwd', name='staff_changepwd'),
		url(r'^(\d+)/$', 'userinfo', name='staff_userinfo')
)
