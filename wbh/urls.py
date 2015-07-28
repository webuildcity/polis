from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView,RedirectView
from django.contrib import admin

from wbc.projects.views import ProjectCreate,ProjectUpdate,ProjectDelete

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/map.html')),
    url(r'^begriffe/$', 'wbc.process.views.process'),
    url(r'^liste/$', 'wbc.projects.views.projects', name='projects'),

    # orte
    url(r'^orte/$', RedirectView.as_view(url='/liste/', permanent=True)),
    url(r'^orte/neu/$', ProjectCreate.as_view(), name='project_create'),
    url(r'^orte/(?P<pk>[0-9]+)/$', 'wbc.projects.views.project', name='project'),
    url(r'^orte/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'wbc.projects.views.projectslug', name='project'),
    
    url(r'^orte/(?P<pk>[0-9]+)/bearbeiten/$', ProjectUpdate.as_view(), name='project_update'),
    url(r'^orte/(?P<pk>[0-9]+)/entfernen/$', ProjectDelete.as_view(), name='project_delete'),

    # veroeffentlichungen neu
    # url(r'^veroeffentlichungen/neu/$', PublicationCreate.as_view(), name='publication_create'),
    # url(r'^veroeffentlichungen/(?P<pk>[0-9]+)/bearbeiten/$', PublicationUpdate.as_view(), name='publication_update'),
    # url(r'^veroeffentlichungen/(?P<pk>[0-9]+)/entfernen/$', PublicationDelete.as_view(), name='publication_delete'),

    # feeds
    # url(r'^feeds/$', 'wbc.core.views.feeds'),
    # url(r'^veroeffentlichungen/feed/$', PublicationFeed(), name="publication_feed_url"),

    # news module
    url(r'^news/abonnieren/$', 'wbc.news.views.subscribe'),
    url(r'^news/abbestellen/(?P<email>.*)$', 'wbc.news.views.unsubscribe'),
    url(r'^news/validieren/(?P<code>.*)$', 'wbc.news.views.validate'),

    # region, process and projects modules, urls by djangorestframework, do not change
    url(r'^region/', include('wbc.region.urls')),
    url(r'^process/', include('wbc.process.urls')),
    url(r'^projects/', include('wbc.projects.urls')),

    # buildings
    # url(r'^buildings/(?P<pk>[0-9]+)/$', 'wbc.buildings.views.building', name='buildings'),

    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # user login
    # url(r'^login/', 'wbc.core.views.login_user'),
    # url(r'^logout/', 'wbc.core.views.logout_user'),

    # serve media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # robots.txt and sitemap.xml
    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain')),

    #rolodex
    # url(r'^rolodex/', include('rolodex.urls')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
