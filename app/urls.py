from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'app.views.index', name='home'),
  (r'^staff/',       include('app.staff.urls')),
  (r'^customer/',    include('app.customer.urls')),
  (r'^item/',        include('app.item.urls')),
  (r'^transaction/', include('app.transaction.urls')),

  # Uncomment the next line to enable the admin:
  (r'^admin/',       include(admin.site.urls)),
)

urlpatterns += patterns('',
  url(r'^static/(?P<path>.*)$',   'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes': True}),
  url(r'^(?P<path>favicon.ico)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes': False}),
)
