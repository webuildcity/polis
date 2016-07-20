from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView,RedirectView
from django.contrib import admin
from django.contrib.auth import views as auth_views

from registration.backends.default.views import RegistrationView, ActivationView

from wbc.core.views import SearchView, StartView
from wbc.projects.views import ProjectCreate,ProjectUpdate,ProjectDelete
from wbc.events.views import PublicationFeed, PublicationCreate, PublicationUpdate,PublicationDelete
from wbc.blog.views import BlogView
from wbc.accounts.views import WbcRegistrationView, RegisterMethodView
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', StartView.as_view(template_name="core/city.html"), name='start'),

    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'wbc.blog.views.blogentry', name='blogentry'),

    # encyclopedia
    url(r'^lexikon/$', 'wbc.encyclopedia.views.encyclopedia', name="encyclopedia"),
    url(r'^lexikon/(?P<pk>[0-9]+)/$', 'wbc.encyclopedia.views.encyclopedia', name="encyclopedia_entry"),

    url(r'^lexikon/$', 'wbc.process.views.process', name="process"),
    url(r'^lexikon/(?P<pk>[0-9]+)/$', 'wbc.process.views.process', name="process_step"),
    url(r'^liste/$', 'wbc.projects.views.projects', name='projects'),

    # projects
    url(r'^projekte/$', RedirectView.as_view(url='/liste/', permanent=True)),
    url(r'^projekt/neu/$', ProjectCreate.as_view(), name='project_create'),
    url(r'^projekt/(?P<pk>[0-9]+)/$', 'wbc.projects.views.project', name='project'),
    url(r'^projekt/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'wbc.projects.views.projectslug', name='projectslug'),

    url(r'^projekt/(?P<pk>[0-9]+)/bearbeiten/$', ProjectUpdate.as_view(), name='project_update'),
    url(r'^projekt/(?P<pk>[0-9]+)/entfernen/$', ProjectDelete.as_view(), name='project_delete'),
    url(r'^projekt/(?P<pk>[0-9]+)/follow/$', 'wbc.projects.views.follow', name='project_follow'),

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
    # url(r'^benutzer/(?P<pk>[0-9]+)$', 'wbc.accounts.views.profile', name='profile'),
    url(r'^benutzerkonto/$', 'wbc.accounts.views.profile_update', name='profile_update'),

    # change password
    url(r'^benutzerkonto/passwort/aendern/$', auth_views.password_change, {
            'template_name': 'accounts/password_change.html'
        }, name='password_change'),
    url(r'^benutzerkonto/passwort/aendern/fertig/$', auth_views.password_change_done, {
            'template_name': 'accounts/password_change_done.html'
        }, name='password_change_done'),

    # reset password
    url(r'^benutzerkonto/passwort/vergessen/$', auth_views.password_reset, {
            'template_name': 'accounts/password_reset_form.html',
            'email_template_name': 'accounts/password_reset_email.txt',
            'subject_template_name': 'accounts/password_reset_subject.txt'
        }, name='password_reset'),
    url(r'^benutzerkonto/passwort/vergessen/info/$', auth_views.password_reset_done, {
            'template_name': 'accounts/password_reset_done.html'
        }, name='password_reset_done'),
    url(r'^benutzerkonto/passwort/vergessen/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {
            'template_name': 'accounts/password_reset_confirm.html'
        }, name='password_reset_confirm'),
    url(r'^benutzerkonto/passwort/vergessen/fertig/$', auth_views.password_reset_complete, {
            'template_name': 'accounts/password_reset_complete.html'
        }, name='password_reset_complete'),

    # register account
    url(r'^register_method/$',RegisterMethodView.as_view(), name="register_method"), 
    url(r'^benutzerkonto/registrieren/$', WbcRegistrationView.as_view(), name='registration_register'),
    url(r'^benutzerkonto/registrieren/abgeschlossen/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^benutzerkonto/aktivieren/abgeschlossen/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
    url(r'^benutzerkonto/aktivieren/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
    url(r'^benutzerkonto/registrieren/geschlossen/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),

    # region, process and projects modules, urls by djangorestframework, do not change
    url(r'^region/', include('wbc.region.urls')),
    url(r'^process/', include('wbc.process.urls')),
    url(r'^events/', include('wbc.events.urls')),
    url(r'^project/', include('wbc.projects.urls')),
    url(r'^stakeholder/', include('wbc.stakeholder.urls')),
    url(r'^blog_api/', include('wbc.blog.urls')),

    # buildings
    # url(r'^buildings/(?P<pk>[0-9]+)/$', 'wbc.buildings.views.building', name='buildings'),

    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # user login
    url(r'^login_wbc/', 'wbc.core.views.login_user', name='login'),
    url(r'^logout/', 'wbc.core.views.logout_user', name='logout'),

    # serve media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # robots.txt and sitemap.xml
    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain')),

    # url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(r'^autocomplete/', 'wbc.core.views.autocomplete', name="autocomplete"),
    url(r'^suche/', SearchView.as_view(), name="search"),
    url(r'^karte/', 'wbc.core.views.map', name="map"),
    # url(r'^suche/', TemplateView.as_view(template_name="core/search.html"), name='search'),

    url(r'^impressum/', TemplateView.as_view(template_name='impressum.html'), name='imprint'),
    url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^tinymce/', include( 'tinymce.urls')),

    url(r'^comments/', include('django_comments.urls')),
    url(r'^comments/post/', 'wbc.core.views.comment_post_wrapper'),

    # translation
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    #ratings
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

    #social auth
    url('', include('social.apps.django_app.urls', namespace='social')),
)
