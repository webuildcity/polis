from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView,RedirectView
from django.contrib import admin
from django.contrib.auth import views as auth_views

from wbc.projects.views import ProjectCreate,ProjectUpdate,ProjectDelete
from wbc.events.views import PublicationFeed, PublicationCreate, PublicationUpdate,PublicationDelete
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/map.html')),

    url(r'^begriffe/$', 'wbc.process.views.process', name="process"),
    url(r'^liste/$', 'wbc.projects.views.projects', name='projects'),

    # projects
    url(r'^projekte/$', RedirectView.as_view(url='/liste/', permanent=True)),
    url(r'^projekt/neu/$', ProjectCreate.as_view(), name='project_create'),
    url(r'^projekt/(?P<pk>[0-9]+)/$', 'wbc.projects.views.project', name='project'),
    url(r'^projekt/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'wbc.projects.views.projectslug', name='projectslug'),

    url(r'^projekt/(?P<pk>[0-9]+)/bearbeiten/$', ProjectUpdate.as_view(), name='project_update'),
    url(r'^projekt/(?P<pk>[0-9]+)/entfernen/$', ProjectDelete.as_view(), name='project_delete'),

    #tags
    url(r'^tags/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'wbc.tags.views.tagview', name='tag'),

    #stakeholder
    url(r'^akteur/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'wbc.stakeholder.views.stakeholderview', name='stakeholder'),

    # veroeffentlichungen neu
    url(r'^veroeffentlichungen/neu/$', PublicationCreate.as_view(), name='publication_create'),
    url(r'^veroeffentlichungen/(?P<pk>[0-9]+)/bearbeiten/$', PublicationUpdate.as_view(), name='publication_update'),
    url(r'^veroeffentlichungen/(?P<pk>[0-9]+)/entfernen/$', PublicationDelete.as_view(), name='publication_delete'),

    # feeds
    url(r'^feeds/$', 'wbc.core.views.feeds'),
    url(r'^veroeffentlichungen/feed/$', PublicationFeed(), name="publication_feed_url"),

    # news module
    url(r'^benachrichtigungen/abonnieren/$', 'wbc.notifications.views.subscribe'),
    url(r'^benachrichtigungen/abbestellen/(?P<email>.*)$', 'wbc.notifications.views.unsubscribe'),
    url(r'^benachrichtigungen/validieren/(?P<code>.*)$', 'wbc.notifications.views.validate'),

    # accounts module
    url(r'^registrieren/$', 'wbc.accounts.views.register'),

    url(r'^passwort/aendern/$', auth_views.password_change, {
            'template_name': 'accounts/password_change.html'
        }, name='password_change'),
    url(r'^passwort/aendern/fertig/$', auth_views.password_change_done, {
            'template_name': 'accounts/password_change_done.html'
        }, name='password_change_done'),
    url(r'^passwort/vergessen/$', auth_views.password_reset, {
            'template_name': 'accounts/password_reset.html',
            'email_template_name': 'accounts/mail/password_reset.html',
            'subject_template_name': 'accounts/mail/password_reset_subject.txt'
        }, name='password_reset'),
    url(r'^passwort/vergessen/info/$', auth_views.password_reset_done, {
            'template_name': 'accounts/password_reset_done.html'
        }, name='password_reset_done'),
    url(r'^passwort/vergessen/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {
            'template_name': 'accounts/password_reset_confirm.html'
        }, name='password_reset_confirm'),
    url(r'^passwort/vergessen/fertig/$', auth_views.password_reset_complete, {
            'template_name': 'accounts/password_reset_complete.html'
        }, name='password_reset_complete'),

    # region, process and projects modules, urls by djangorestframework, do not change
    url(r'^region/', include('wbc.region.urls')),
    url(r'^process/', include('wbc.process.urls')),
    url(r'^events/', include('wbc.events.urls')),
    url(r'^project/', include('wbc.projects.urls')),
    url(r'^stakeholder/', include('wbc.stakeholder.urls')),

    # buildings
    # url(r'^buildings/(?P<pk>[0-9]+)/$', 'wbc.buildings.views.building', name='buildings'),

    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # user login
    url(r'^login/', 'wbc.core.views.login_user', name='login'),
    url(r'^logout/', 'wbc.core.views.logout_user', name='logout'),

    # serve media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # robots.txt and sitemap.xml
    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain')),

    # url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),

    # url(r'^autocomplete/', 'wbc.core.views.autocomplete'),
    # url(r'^suche/', 'wbc.core.views.search', name='search'),

)
