from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from mysite import settings

urlpatterns = patterns ('',
    url(r'^meeting/', include('meeting.urls', namespace='meeting')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_static/(?P<path>.*)$','django.views.static.serve', {'document_root':'/Users/yug/mysite/sitestatic', 'show_indexes': True}),

)
