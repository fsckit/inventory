from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Route for home page
  url(r'^$', 'app.views.index', name='home'),
  # Basic routes that extend to each of the submodules in the app
  (r'^staff/',       include('app.staff.urls')),
  (r'^customer/',    include('app.customer.urls')),
  (r'^item/',        include('app.item.urls')),
  (r'^transaction/', include('app.transaction.urls')),
  (r'^search/',      include('app.search.urls')),
  # Route for history updates
  (r'^socket\.io/', 'app.views.subscribe'),

  # Uncomment the next line to enable the admin:
  (r'^admin/',       include(admin.site.urls)),
)

# Static elements
urlpatterns += patterns('',
  url(r'^static/(?P<path>.*)$',   'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes': True}),
  url(r'^(?P<path>favicon.ico)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes': False}),
)
