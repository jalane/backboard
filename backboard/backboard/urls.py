from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^backboard/errorgen/([0-9]{3})/$', 'errorgen.views.renderError'),
    url(r'^backboard/sahara/$', 'sahara.views.index'),
)
